# 🌤️🕒 Multi Tool Agent

A simple AI agent built with [Google's Agent Development Kit (ADK)](https://github.com/google/generative-ai-docs/tree/main/tools/agent-development-kit) that responds to user queries about the **weather** and **current time** in specific cities. The agent uses tool functions defined in Python and supports multiple AI models including Gemini, GPT-4, and Claude via LiteLLM integration.

---

## 🗂️ Project Structure

```
multi_tool_agent/
├── __init__.py       # Module initializer
├── agent.py          # Core agent definition and tool functions
├── agent.ipynb       # Jupyter notebook with multi-model implementation
├── .env              # Environment variables (API keys)
├── .gitignore        # Prevents secrets and compiled files from being committed
```

---

## ✅ Features

- ✅ Responds with weather reports for supported cities (e.g., New York)
- ✅ Returns the current time for supported timezones (e.g., America/New_York)
- ✅ Modular tool function design
- ✅ Runs locally with dev UI or CLI
- ✅ Multi-model support via LiteLLM (Gemini, GPT-4, Claude)
- ✅ Jupyter notebook implementation for easy experimentation

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/maniaclab/multi_tool_agent.git
cd multi_tool_agent
```

### 2. Set Up a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install google-adk litellm python-dotenv
```

---

## 🔐 Environment Variables

Create a `.env` file in the `multi_tool_agent/` folder:

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your_google_ai_studio_key_here
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

> ⚠️ **Never commit `.env` to version control.** It contains secrets.

---

## 🧠 Usage

### Run via Jupyter Notebook

1. Start Jupyter:
```bash
jupyter notebook
```

2. Open `agent.ipynb` and run the cells sequentially to:
   - Set up the environment
   - Configure multiple AI models
   - Create and test the weather agent
   - Run interactive conversations

### Run the agent via interactive Dev UI

```bash
adk web
```

Then open `http://localhost:8080` in your browser to chat with the agent.

### Or run in terminal:

```bash
adk run
```

---

## 🤖 Supported Models

The agent supports multiple AI models through LiteLLM integration:

- Gemini: `gemini-2.0-flash`
- GPT-4: `openai/gpt-4.1`
- Claude: `anthropic/claude-sonnet-4-20250514`

You can easily switch between models by modifying the `AGENT_MODEL` constant in the code.

---

## 🔒 .gitignore

This repo uses `.gitignore` to prevent committing sensitive or unnecessary files:

```
.venv/
.env
__pycache__/
.ipynb_checkpoints/
```

If `.env` or cache files were already committed:
```bash
git rm --cached .env
git commit -m "Remove tracked .env file"
```

---

## 📌 Notes

- The agent currently only supports:
  - Weather: `New York` (add more manually or via API)
  - Time: `New York` (ZoneInfo support for more cities)
- You can extend the agent by:
  - Adding real weather APIs like OpenWeatherMap
  - Supporting more timezones
  - Defining additional tools
  - Adding more AI models through LiteLLM

---

## 📚 References

- [Google ADK Docs](https://github.com/google/generative-ai-docs/tree/main/tools/agent-development-kit)
- [Google AI Studio](https://aistudio.google.com)
- [Python `zoneinfo`](https://docs.python.org/3/library/zoneinfo.html)
- [LiteLLM Documentation](https://docs.litellm.ai)

---

## 👨‍💻 Author

Built by [Akash Pai](https://github.com/Akash-N-Pai) for learning and experimentation with Google's ADK and Gemini APIs.

---

## 🪪 License

This project is licensed under the MIT License.
