import os
import asyncio
import logging
import warnings
from typing import Optional, Dict, Any
import requests
from dotenv import load_dotenv

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types
from google.adk.tools.tool_context import ToolContext
from google.adk.agents.callback_context import CallbackContext
from google.adk.models.llm_request import LlmRequest
from google.adk.models.llm_response import LlmResponse
from google.adk.tools.base_tool import BaseTool

# --- Setup ---
load_dotenv()
warnings.filterwarnings("ignore")
logging.basicConfig(level=logging.ERROR)

# --- Model Constants ---
MODEL_GEMINI_2_0_FLASH = "gemini-2.0-flash"
MODEL_GPT_4O = "openai/gpt-4.1"
MODEL_CLAUDE_SONNET = "anthropic/claude-sonnet-4-20250514"

# --- Weather Tool (OpenWeatherMap API) ---
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
OPENWEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city: str) -> dict:
    """Fetches real weather data for any city using OpenWeatherMap API."""
    if not OPENWEATHER_API_KEY:
        return {"status": "error", "error_message": "OpenWeatherMap API key not set in .env."}
    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"
    }
    try:
        resp = requests.get(OPENWEATHER_URL, params=params, timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            temp_c = data["main"]["temp"]
            condition = data["weather"][0]["description"].capitalize()
            report = f"The weather in {city} is {condition} with a temperature of {temp_c:.1f}°C."
            return {"status": "success", "report": report}
        else:
            return {"status": "error", "error_message": f"Weather API error: {resp.json().get('message', 'Unknown error')}"}
    except Exception as e:
        return {"status": "error", "error_message": f"Weather API exception: {e}"}

# --- Stateful Weather Tool ---
def get_weather_stateful(city: str, tool_context: ToolContext) -> dict:
    """Fetches weather and formats temp based on session state (C/F)."""
    preferred_unit = tool_context.state.get("user_preference_temperature_unit", "Celsius")
    result = get_weather(city)
    if result["status"] == "success":
        # Convert to Fahrenheit if needed
        if preferred_unit == "Fahrenheit":
            import re
            import math
            match = re.search(r"([-+]?[0-9]*\.?[0-9]+)°C", result["report"])
            if match:
                temp_c = float(match.group(1))
                temp_f = temp_c * 9/5 + 32
                result["report"] = result["report"].replace(f"{temp_c:.1f}°C", f"{math.ceil(temp_f)}°F")
        tool_context.state["last_city_checked_stateful"] = city
    return result

# --- Greeting & Farewell Tools ---
def say_hello(name: Optional[str] = None) -> str:
    if name:
        return f"Hello, {name}!"
    return "Hello there!"

def say_goodbye() -> str:
    return "Goodbye! Have a great day."

# --- Guardrail Callbacks ---
def block_keyword_guardrail(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    last_user_message_text = ""
    if llm_request.contents:
        for content in reversed(llm_request.contents):
            if content.role == 'user' and content.parts and content.parts[0].text:
                last_user_message_text = content.parts[0].text
                break
    if "BLOCK" in last_user_message_text.upper():
        callback_context.state["guardrail_block_keyword_triggered"] = True
        return LlmResponse(
            content=types.Content(
                role="model",
                parts=[types.Part(text="I cannot process this request because it contains the blocked keyword 'BLOCK'.")],
            )
        )
    return None

def block_paris_tool_guardrail(tool: BaseTool, args: Dict[str, Any], tool_context: ToolContext) -> Optional[Dict]:
    if tool.name == "get_weather_stateful":
        city_argument = args.get("city", "")
        if city_argument and city_argument.lower() == "paris":
            tool_context.state["guardrail_tool_block_triggered"] = True
            return {
                "status": "error",
                "error_message": f"Policy restriction: Weather checks for '{city_argument.capitalize()}' are currently disabled by a tool guardrail."
            }
    return None

# --- Sub-Agents ---
greeting_agent = Agent(
    model=MODEL_GEMINI_2_0_FLASH,
    name="greeting_agent",
    instruction="You are the Greeting Agent. ONLY greet using the 'say_hello' tool.",
    description="Handles greetings.",
    tools=[say_hello],
)

farewell_agent = Agent(
    model=MODEL_GEMINI_2_0_FLASH,
    name="farewell_agent",
    instruction="You are the Farewell Agent. ONLY say goodbye using the 'say_goodbye' tool.",
    description="Handles farewells.",
    tools=[say_goodbye],
)

# --- Root Agent ---
root_agent = Agent(
    name="weather_agent_full",
    model=MODEL_GEMINI_2_0_FLASH,
    description="Main agent: Provides real weather, delegates greetings/farewells, stateful, with guardrails.",
    instruction="You are the main Weather Agent. Use 'get_weather_stateful' for weather. Delegate greetings/farewells. Block 'Paris' and 'BLOCK' as per policy.",
    tools=[get_weather_stateful],
    sub_agents=[greeting_agent, farewell_agent],
    output_key="last_weather_report",
    before_model_callback=block_keyword_guardrail,
    before_tool_callback=block_paris_tool_guardrail,
)

# --- Session Service & Runner ---
APP_NAME = "weather_tutorial_app_full"
USER_ID = "user_1_full"
SESSION_ID = "session_001_full"
initial_state = {"user_preference_temperature_unit": "Celsius"}
session_service = InMemorySessionService()

# --- Agent Interaction Function ---
async def call_agent_async(query: str, runner, user_id, session_id):
    print(f"\n>>> User Query: {query}")
    content = types.Content(role='user', parts=[types.Part(text=query)])
    final_response_text = "Agent did not produce a final response."
    async for event in runner.run_async(user_id=user_id, session_id=session_id, new_message=content):
        if event.is_final_response():
            if event.content and event.content.parts:
                final_response_text = event.content.parts[0].text
            elif event.actions and event.actions.escalate:
                final_response_text = f"Agent escalated: {event.error_message or 'No specific message.'}"
            break
    print(f"<<< Agent Response: {final_response_text}")

# --- Main Conversation Loop ---
async def main():
    session = await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
        state=initial_state
    )
    runner = Runner(
        agent=root_agent,
        app_name=APP_NAME,
        session_service=session_service
    )
    await call_agent_async("Hello!", runner, USER_ID, SESSION_ID)
    await call_agent_async("What's the weather in New York?", runner, USER_ID, SESSION_ID)
    await call_agent_async("How about Paris?", runner, USER_ID, SESSION_ID)
    await call_agent_async("Tell me the weather in London.", runner, USER_ID, SESSION_ID)
    await call_agent_async("BLOCK the request for weather in Tokyo", runner, USER_ID, SESSION_ID)
    await call_agent_async("Thanks, bye!", runner, USER_ID, SESSION_ID)

if __name__ == "__main__":
    asyncio.run(main()) 