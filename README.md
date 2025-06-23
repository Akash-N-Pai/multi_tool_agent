# 🌤️�� Multi Tool Agent

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

A showcase of AI agents built with [Google's Agent Development Kit (ADK)](https://github.com/google/generative-ai-docs/tree/main/tools/agent-development-kit).

This repo includes:
- A **simple agent** for weather and time in New York (demo/learning)
- A **full-featured agent** with real weather, interactive CLI, guardrails, and user preferences

---

## 🗂️ Project Structure

```
multi_tool_agent/
├── .gitignore                # Ignores .env and __pycache__ in root
├── .env                      # (optional) Environment variables for root agent
├── agent/                    # Package version of simple agent
│   ├── agent.py              # Simple agent (mock, New York only, standalone script)
│   ├── __init__.py
│   ├── .gitignore            # Ignores .env in this folder
│   └── README_agent.md       # Usage and details for the simple agent
├── full_agent/               # Full-featured, production-ready agent
│   ├── full_agent.py
│   ├── __init__.py
│   ├── .gitignore            # Ignores .env in this folder
│   └── README_full_agent.md  # Usage and details for the full agent
├── agent.ipynb               # Jupyter notebook (learning resource only)
├── __pycache__/              # Python bytecode cache (ignored by git)
└── README.md                 # This file
```

---

## ✅ Features

### Simple Agent (`agent.py` or `agent/agent.py`)
- Returns a mock weather report for New York
- Returns the current time in New York
- Minimal ADK example, easy to extend
- Use as a standalone script or as a package

### Full Agent (`full_agent/full_agent.py`)
- Fetches **real weather** for any city (OpenWeatherMap API)
- Interactive CLI: type queries, change units, or exit
- Sub-agents for greetings and farewells
- Guardrails: block certain cities/keywords (configurable)
- Remembers user temperature unit preference (Celsius/Fahrenheit)
- All config via `.env` (API keys, blocked cities, etc.)
- Logging for all output

---

## 🚀 Quick Start

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
pip install google-adk litellm python-dotenv requests
```

---

## 🧠 Usage

### Simple Agent (Demo)
- See [`agent.py`](./agent.py) or [`agent/README_agent.md`](./agent/README_agent.md)
- Example:
  ```python
  from agent import root_agent
  print(root_agent.tools[0]("New York"))  # Weather
  print(root_agent.tools[1]("New York"))  # Time
  ```
- **Note:** Only supports "New York"; weather is mock data.
- **Note:** `agent.py` and `agent/agent.py` are functionally the same for demo purposes.

### Full Agent (Production/Interactive)
- See [`full_agent/full_agent.py`](./full_agent/full_agent.py) or [`full_agent/README_full_agent.md`](./full_agent/README_full_agent.md)
- Create a `.env` file in `full_agent/` (see the full agent README for details)
- Run:
  ```bash
  python full_agent/full_agent.py
  ```
- Type queries like:
  - `What's the weather in London?`
  - `set unit to fahrenheit`
  - `exit`

### Jupyter Notebook (Learning Only)
- `agent.ipynb` is for step-by-step experimentation and learning. Not intended for production use.

---

## 🔐 Environment Variables & .gitignore

- Each agent folder can have its own `.env` and `.gitignore` (recommended for secrets isolation)
- Example for `full_agent/.env`:
  ```
  OPENWEATHER_API_KEY=your_openweathermap_api_key_here
  BLOCKED_CITIES=paris,moscow
  ...
  ```
- **Never commit `.env` files to git!**  
  All `.gitignore` files in this repo are set up to ignore `.env` and cache files in their respective folders.

---

## 📸 Demo Screenshots

*Coming soon!*

---

## 📚 References & More Info

- [Simple Agent README](./agent/README_agent.md)
- [Full Agent README](./full_agent/README_full_agent.md)
- [Google ADK Docs](https://github.com/google/generative-ai-docs/tree/main/tools/agent-development-kit)
- [OpenWeatherMap API](https://openweathermap.org/api)
- [LiteLLM Documentation](https://docs.litellm.ai)

---

## 👨‍💻 Author

Built by [Akash Pai](https://github.com/Akash-N-Pai) for learning and experimentation with Google's ADK and Gemini APIs.

---

## 🤝 Contributing

Contributions, issues, and suggestions are welcome! Please open an issue or pull request.

---

## 🪪 License

This project is licensed under the MIT License.
