# 🌤️🕒 Multi Tool Agent

A simple AI agent built with [Google's Agent Development Kit (ADK)](https://github.com/google/generative-ai-docs/tree/main/tools/agent-development-kit) that responds to user queries about the **weather** and **current time** in specific cities. The agent uses tool functions defined in Python and is configured to run locally with Gemini models via Google AI Studio.

---

## 🗂️ Project Structure

```
multi_tool_agent/
├── __init__.py       # Module initializer
├── agent.py          # Core agent definition and tool functions
├── .env              # Environment variables (API keys)
├── .gitignore        # Prevents secrets and compiled files from being committed
```

---

## ✅ Features

- ✅ Responds with weather reports for supported cities (e.g., New York)
- ✅ Returns the current time for supported timezones (e.g., America/New_York)
- ✅ Modular tool function design
- ✅ Runs locally with dev UI or CLI

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Akash-N-Pai/multi_tool_agent.git
cd multi_tool_agent
```

### 2. Set Up a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install google-adk
```

---

## 🔐 Environment Variables

Create a `.env` file in the `multi_tool_agent/` folder:

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your_google_ai_studio_key_here
```

> ⚠️ **Never commit `.env` to version control.** It contains secrets.

---

## 🧠 Usage

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

## 🔒 .gitignore

This repo uses `.gitignore` to prevent committing sensitive or unnecessary files:

```
.venv/
.env
__pycache__/
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

---

## 📚 References

- [Google ADK Docs](https://github.com/google/generative-ai-docs/tree/main/tools/agent-development-kit)
- [Google AI Studio](https://aistudio.google.com)
- [Python `zoneinfo`](https://docs.python.org/3/library/zoneinfo.html)

---

## 👨‍💻 Author

Built by [Akash Pai](https://github.com/Akash-N-Pai) for learning and experimentation with Google’s ADK and Gemini APIs.

---

## 🪪 License

This project is licensed under the MIT License.
