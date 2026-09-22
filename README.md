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

**Concept: Parallel Agent (Fan-out)**

A `ParallelAgent` runs all its sub-agents **simultaneously**. Each sub-agent writes to its own `output_key` in state so results never overwrite each other. A downstream aggregator agent then reads all those keys and compiles a single response.

```python
from google.adk.agents.parallel_agent import ParallelAgent

# each finder saves to its own state key
museum_finder_agent  = Agent(..., output_key="museum_result")
concert_finder_agent = Agent(..., output_key="concert_result")
restaurant_finder_agent = Agent(..., output_key="restaurant_result")

# all three run at the same time
parallel_research_agent = ParallelAgent(
    name="parallel_research_agent",
    sub_agents=[museum_finder_agent, concert_finder_agent, restaurant_finder_agent],
)

# aggregator reads all three keys and combines them
aggregator_agent = Agent(
    name="aggregator_agent",
    instruction="Compile the results from {museum_result}, {concert_result}, {restaurant_result}...",
)

# research in parallel, then aggregate
root_agent = SequentialAgent(
    name="city_explorer",
    sub_agents=[parallel_research_agent, aggregator_agent],
)
```

---

## What's in This Branch

| Folder | Description |
|--------|-------------|
| `basic_chat_bot/` | Basic agent (branch 000) |
| `day_trip_agent/` | Day trip planner with Google Search (branch 001) |
| `weather_aware_planner/` | Custom-tool weather planner (branch 002) |
| `trip_concierge/` | Orchestrator with nested agents (branch 003) |
| `router_agent/` | Router + SequentialAgent pipeline (branch 005) |
| `loop_planner/` | LoopAgent critic-refiner loop (branch 006) |
| `city_explorer/` | **New** — ParallelAgent that fans out to three finders, then aggregates |

---

## Run an Agent

```bash
adk web city_explorer
```

Open [http://localhost:8000](http://localhost:8000) in your browser.

## Things to Try (with `city_explorer`)

- `"What's there to do in Manila this weekend?"`
- `"Give me a city guide for Tokyo."`
- `"I'm visiting New York next week — what should I see, hear, and eat?"`

Watch three agents fire simultaneously (museums, concerts, restaurants), then the aggregator compile everything into one city guide.

---

## Navigate Branches

```bash
git checkout 008-agent-skills    # next: custom skills for file I/O
git checkout 006-loop-agent      # back
```
