# Google ADK Workshop

Welcome! In this workshop you'll build a series of AI agents using Google's **Agent Development Kit (ADK)**. Each branch introduces a new concept, and every branch builds on the one before it.

## Branch Progression

| Branch | Concept |
|--------|---------|
| `000-basic-agent` | The skeleton — a minimal agent that answers questions |
| `001-agent-with-tool` | Giving an agent a built-in tool (Google Search) |
| `002-agent-custom-tool` | Writing your own Python function as a tool |
| `003-orchestrator` | One agent delegating to specialist sub-agents |
| `004-router` | A router that picks the right agent for each request |
| `005-sequential` | A sequential pipeline + agents split into their own folders |

---

## One-Time Setup

Do this once after cloning. Your setup persists across all branch switches.

### 1. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate    # Mac / Linux
# .venv\Scripts\activate     # Windows
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create your API key file

```bash
cp .env.example .env
```

Open `.env` and replace `your_api_key_here` with your key from [Google AI Studio](https://aistudio.google.com/apikey).

---

## What's New in This Branch

**Concept: Built-in Tools**

Tools let an agent take **actions** beyond just generating text. The most useful built-in tool is `google_search`, which gives the agent access to real-time information from the internet.

```python
from google.adk.tools import google_search

root_agent = Agent(
    name="day_trip_agent",
    tools=[google_search],   # ← the only change from branch 000
)
```

The agent now decides *on its own* when to search — it calls the tool mid-response whenever it needs current information.

---

## What's in This Branch

| Folder | Description |
|--------|-------------|
| `basic_chat_bot/` | The same basic agent from branch 000 (no tools) |
| `day_trip_agent/` | **New** — a day trip planner with Google Search |

---

## Run an Agent

```bash
# Run the basic chat bot (familiar from branch 000)
adk web basic_chat_bot

# Run the day trip planner ← try this one to see tools in action
adk web day_trip_agent
```

Open [http://localhost:8000](http://localhost:8000) in your browser.

## Things to Try (with `day_trip_agent`)

- `"Plan me a fun day trip to San Francisco on a $50 budget."`
- `"I want a relaxing day near the ocean. What do you suggest?"`
- `"Plan an adventurous day trip for someone who loves hiking."`

Watch the agent **call Google Search automatically** to find current info, hours, and events.

---

## Navigate Branches

```bash
git checkout 002-agent-custom-tool   # next: write your own tool
git checkout 000-basic-agent         # back
```
