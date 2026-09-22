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
| `005-sequential` | A sequential pipeline (SequentialAgent) |
| `006-loop-agent` | An iterative refinement loop (LoopAgent) |
| `007-parallel-agent` | Parallel research with fan-out (ParallelAgent) |
| `008-agent-skills` | Custom tool functions (skills) for file I/O |

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

**Concept: Custom Tools**

In the previous branch, the agent used a built-in tool from ADK. Here, you write your own Python function and hand it directly to the agent.

Any regular Python function becomes a tool — ADK reads the function name, docstring, and type hints to teach the agent how and when to call it.

```python
def get_live_weather_forecast(location: str) -> dict:
    """Gets the current, real-time weather forecast for a specified location."""
    # your Python code here — calls the NWS API
    ...

root_agent = Agent(
    name="weather_aware_planner",
    tools=[get_live_weather_forecast],   # ← just pass the function
)
```

The agent now calls your function automatically whenever the user asks about weather or outdoor plans.

---

## What's in This Branch

| Folder | Description |
|--------|-------------|
| `basic_chat_bot/` | Basic agent (branch 000) |
| `day_trip_agent/` | Day trip planner with Google Search (branch 001) |
| `weather_aware_planner/` | **New** — trip planner that checks live weather before suggesting activities |

---

## Run an Agent

```bash
# Run the weather-aware trip planner ← try this one
adk web weather_aware_planner

# Or the day trip planner from branch 001
adk web day_trip_agent
```

Open [http://localhost:8000](http://localhost:8000) in your browser.

## Things to Try (with `weather_aware_planner`)

- `"Should I go hiking near Sunnyvale today?"`
- `"Plan an outdoor activity in San Francisco this afternoon."`
- `"Is it a good day for a trip to Lake Tahoe?"`

Watch the agent call `get_live_weather_forecast` and incorporate the result into its answer.

---

## Navigate Branches

```bash
git checkout 003-orchestrator          # next: agents delegating to other agents
git checkout 001-agent-with-tool       # back
```
