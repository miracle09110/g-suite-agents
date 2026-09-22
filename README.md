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

**Concept: Loop Agent (Iterative Refinement)**

A `LoopAgent` runs its sub-agents in a cycle, up to `max_iterations` times. Any sub-agent can call the built-in `exit_loop` tool to stop early once the output is good enough.

```python
from google.adk.agents.loop_agent import LoopAgent
from google.adk.tools.exit_loop_tool import exit_loop

# critic calls exit_loop when the plan is strong enough
critic_agent = Agent(name="critic_agent", tools=[exit_loop], ...)

# refiner rewrites the plan based on the critique
refiner_agent = Agent(name="refiner_agent", ...)

# runs critic → refiner up to 3 times (stops early if critic is satisfied)
refinement_loop = LoopAgent(
    name="refinement_loop",
    sub_agents=[critic_agent, refiner_agent],
    max_iterations=3,
)

# root: draft first, then loop to refine
root_agent = SequentialAgent(
    name="loop_planner",
    sub_agents=[planner_agent, refinement_loop],
)
```

The planner drafts an initial plan; the loop then runs critic → refiner up to three times. The critic calls `exit_loop` as soon as the plan is solid, so the loop often finishes in fewer than three rounds.

---

## What's in This Branch

| Folder | Description |
|--------|-------------|
| `basic_chat_bot/` | Basic agent (branch 000) |
| `day_trip_agent/` | Day trip planner with Google Search (branch 001) |
| `weather_aware_planner/` | Custom-tool weather planner (branch 002) |
| `trip_concierge/` | Orchestrator with nested agents (branch 003) |
| `router_agent/` | Router + SequentialAgent pipeline (branch 005) |
| `loop_planner/` | **New** — LoopAgent that drafts then iteratively refines a plan |

---

## Run an Agent

```bash
adk web loop_planner
```

Open [http://localhost:8000](http://localhost:8000) in your browser.

## Things to Try (with `loop_planner`)

- `"Plan a product launch for a mobile app."`
- `"Create a 30-day study plan for learning Python."`
- `"Plan a community fundraising event."`

Watch the critic evaluate each draft and either call `exit_loop` (done) or list weaknesses for the refiner to fix.

---

## Navigate Branches

```bash
git checkout 007-parallel-agent    # next: parallel fan-out with ParallelAgent
git checkout 005-sequential        # back
```
