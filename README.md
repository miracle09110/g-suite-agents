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
| `005-sequential` | A pipeline where agents run in sequence, passing results forward |
| `005.5-sequential-folder-restructure` | Refactoring agents into a clean folder structure |

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

**Concept: Orchestrator Pattern**

So far, one agent does everything. The orchestrator pattern splits responsibility: a top-level agent receives requests and **delegates work to specialist sub-agents**, each expert at one thing.

```
User
 └─> trip_data_concierge (orchestrator)
       ├─> call_db_agent       — fetches hotel/landmark data
       └─> call_concierge_agent
             └─> food_critic_agent  — gives restaurant opinions
```

The orchestrator in `trip_concierge/` calls two async tool-functions. One fetches data from a mock database; the other asks a concierge agent (which in turn asks a food critic agent) for a recommendation. Results flow through `tool_context.state` so each step can read what the previous one found.

---

## What's in This Branch

| Folder | Description |
|--------|-------------|
| `basic_chat_bot/` | Basic agent (branch 000) |
| `day_trip_agent/` | Day trip planner with Google Search (branch 001) |
| `weather_aware_planner/` | Custom-tool weather planner (branch 002) |
| `trip_concierge/` | **New** — orchestrator that chains a DB agent and a concierge agent |

---

## Run an Agent

```bash
# Run the orchestrator ← try this one
adk web trip_concierge

# Or any previous agent
adk web day_trip_agent
```

Open [http://localhost:8000](http://localhost:8000) in your browser.

## Things to Try (with `trip_concierge`)

- `"Find me a hotel and then suggest a restaurant nearby."`
- `"What are the top-rated hotels, and where should I eat after checking in?"`

Watch the agent call `call_db_agent` first, then `call_concierge_agent` with the retrieved data — two agents coordinating automatically.

---

## Navigate Branches

```bash
git checkout 004-router                # next: routing between agents
git checkout 002-agent-custom-tool     # back
```
