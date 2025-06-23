# 🌤️🤖 Full-Featured ADK Weather Agent

This project provides a fully-featured conversational AI agent using [Google's Agent Development Kit (ADK)](https://github.com/google/generative-ai-docs/tree/main/tools/agent-development-kit). The agent can:
- Fetch real-time weather for any city using the OpenWeatherMap API
- Greet and say goodbye using sub-agents
- Enforce guardrails (block certain cities or keywords)
- Remember user preferences (Celsius/Fahrenheit)
- Run interactively in your terminal

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd multi_tool_agent
```

### 2. Set Up a Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install google-adk litellm python-dotenv requests
```

### 4. Configure Environment Variables
Create a `.env` file in the `multi_tool_agent/` folder:
```
OPENWEATHER_API_KEY=your_openweathermap_api_key_here
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your_google_ai_studio_key_here
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
BLOCKED_CITIES=paris  # Comma-separated list of cities to block (optional)
```
- Get a free API key from [OpenWeatherMap](https://openweathermap.org/).
- You can block multiple cities: `BLOCKED_CITIES=paris,moscow`

### 5. Run the Agent
```bash
python full_agent.py
```

---

## 🧠 Features
- **Real Weather:** Fetches live weather for any city using OpenWeatherMap
- **Greetings & Farewells:** Specialized sub-agents for hello/goodbye
- **Guardrails:**
  - Blocks queries for cities in `BLOCKED_CITIES`
  - Blocks queries containing the word `BLOCK`
- **Session State:** Remembers your temperature unit preference (Celsius/Fahrenheit)
- **Interactive CLI:** Type queries, change units, or exit at any time
- **Configurable:** All keys and settings via `.env`
- **Logging:** All output uses Python logging for easy debugging

---

## 💬 Usage
- **Ask for weather:**
  - `What's the weather in London?`
  - `Tell me the weather in Tokyo.`
- **Change temperature unit:**
  - `set unit to fahrenheit`
  - `set unit to celsius`
- **Greetings/Farewells:**
  - `Hello!`
  - `Thanks, bye!`
- **Exit:**
  - `exit` or `quit`

---

## ⚙️ Configuration
- **API Keys:** Required for OpenWeatherMap and (optionally) for Gemini, OpenAI, Anthropic
- **Blocked Cities:** Set `BLOCKED_CITIES` in `.env` (comma-separated)
- **Default Unit:** Starts in Celsius; user can change at runtime

---

## 🛠️ Troubleshooting
- **Missing API Key:**
  - If you see an error about `OPENWEATHER_API_KEY`, add it to your `.env` file.
- **City Not Found:**
  - The agent will inform you if the city is not recognized by OpenWeatherMap.
- **Blocked City:**
  - If you ask for a blocked city, you'll get a policy error message.
- **No Response:**
  - Check your API keys and internet connection.

---

## 📚 References
- [Google ADK Documentation](https://github.com/google/generative-ai-docs/tree/main/tools/agent-development-kit)
- [OpenWeatherMap API](https://openweathermap.org/api)
- [LiteLLM Documentation](https://docs.litellm.ai)

---

## 👨‍💻 Author
Built by [Akash Pai](https://github.com/Akash-N-Pai) and enhanced with best practices for robust, extensible AI agents. 