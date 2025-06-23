# 🕒🌤️ Simple ADK Weather & Time Agent (`agent.py`)

This module provides a minimal example of an AI agent using [Google's Agent Development Kit (ADK)](https://github.com/google/generative-ai-docs/tree/main/tools/agent-development-kit). The agent can:
- Return a mock weather report for New York
- Return the current time in New York

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install google-adk
```

### 2. Usage
This file defines an agent named `weather_time_agent` with two tools:
- `get_weather(city: str)` — Returns a mock weather report for New York
- `get_current_time(city: str)` — Returns the current time for New York

**Example usage in Python:**
```python
from agent import root_agent

# Call the weather tool directly
print(root_agent.tools[0]("New York"))
# Call the time tool directly
print(root_agent.tools[1]("New York"))
```

> **Note:** This agent is designed for demonstration and does not connect to real APIs. It only supports "New York" as a valid city.

---

## 🧠 Features
- **Weather:** Returns a static, hardcoded weather report for New York
- **Time:** Returns the actual current time in New York (using Python's `zoneinfo`)
- **ADK Agent:** Ready to be used with ADK runners or extended with more tools

---

## ⚠️ Limitations
- Only supports the city "New York" (all other cities return an error)
- Weather data is not real-time or dynamic
- No session state, sub-agents, or guardrails

---

## 📚 References
- [Google ADK Documentation](https://github.com/google/generative-ai-docs/tree/main/tools/agent-development-kit)
- [Python `zoneinfo`](https://docs.python.org/3/library/zoneinfo.html)

---

## 👨‍💻 Author
Built for learning and experimentation with Google's ADK. 