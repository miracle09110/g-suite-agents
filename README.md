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

**Concept 1: Sequential Agent (Pipeline)**

A `SequentialAgent` runs a list of sub-agents **one after another**, automatically passing each agent's output as context to the next. This is the pipeline pattern.

```python
from google.adk.agents.sequential_agent import SequentialAgent

find_and_navigate_agent = SequentialAgent(
    name="find_and_navigate_agent",
    sub_agents=[foodie_agent, transportation_agent],
)
```

Here, `foodie_agent` finds the best restaurant and saves its answer to `state['destination']`. Then `transportation_agent` automatically reads that destination from state and gives directions — no manual wiring needed.

**Concept 2: Clean Folder Structure**

Each sub-agent now lives in its own folder inside `router_agent/`. The main `agent.py` just imports and wires them together — no definitions inline.

```
router_agent/
  agent.py                 ← router + imports only
  day_trip_agent/
  foodie_agent/
  transportation_agent/
  weekend_guide_agent/
  find_and_navigate_agent/
```

This is the structure you'd use in a real project as the number of agents grows.

---

## What's in This Branch

| Folder | Description |
|--------|-------------|
| `basic_chat_bot/` | Basic agent (branch 000) |
| `day_trip_agent/` | Day trip planner with Google Search (branch 001) |
| `weather_aware_planner/` | Custom-tool weather planner (branch 002) |
| `trip_concierge/` | Orchestrator with nested agents (branch 003) |
| `router_agent/` | **Updated** — sequential pipeline added, each sub-agent in its own folder |

---

## Run an Agent

```bash
# Run the router (which now includes the sequential pipeline)
adk web router_agent
```

Open [http://localhost:8000](http://localhost:8000) in your browser.

## Things to Try (with `router_agent`)

- `"Find the best sushi near Palo Alto and give me directions from San Francisco."` → triggers the sequential pipeline: find → navigate
- `"What's good to eat in downtown SF?"` → routes to `foodie_agent` directly (no pipeline needed)
- `"Plan a day trip to Napa."` → routes to `day_trip_agent`

For the first prompt, watch two agents fire in sequence: the foodie agent picks the restaurant, then the navigation agent gives directions to that exact place.

---

## You've reached the end of the workshop!

You now know the core ADK patterns:

| Pattern | What it does |
|---------|-------------|
| Basic Agent | LLM with instructions |
| Built-in Tool | Extends an agent with ready-made capabilities (Search) |
| Custom Tool | Any Python function becomes a tool |
| Orchestrator | Coordinates multiple agents for complex tasks |
| Router | Picks the right specialist for each request |
| Sequential | Chains agents in a pipeline, passing results forward |
| Folder structure | Keeps multi-agent projects maintainable |

---

## Navigate Branches

```bash
git checkout 004-router    # back
```
