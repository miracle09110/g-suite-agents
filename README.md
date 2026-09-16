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

**Concept: Router Pattern**

In the orchestrator pattern, one agent always calls the same sub-agents. The router pattern is different: a top-level agent reads the user's request and **decides which specialist agent is the best fit**, then forwards the request to that one.

```
User
 └─> router_agent (decides based on intent)
       ├─> foodie_agent         — "where should I eat?"
       ├─> weekend_guide_agent  — "what's happening this weekend?"
       └─> day_trip_agent       — everything else
```

The router doesn't answer questions directly — it reads the request, picks a specialist, and returns that agent's response.

---

## What's in This Branch

| Folder | Description |
|--------|-------------|
| `basic_chat_bot/` | Basic agent (branch 000) |
| `day_trip_agent/` | Day trip planner with Google Search (branch 001) |
| `weather_aware_planner/` | Custom-tool weather planner (branch 002) |
| `trip_concierge/` | Orchestrator with nested agents (branch 003) |
| `router_agent/` | **New** — routes requests to foodie, weekend guide, or day trip specialists |

---

## Run an Agent

```bash
# Run the router ← try this one
adk web router_agent

# Or any previous agent
adk web trip_concierge
```

Open [http://localhost:8000](http://localhost:8000) in your browser.

## Things to Try (with `router_agent`)

- `"What's the best ramen place near downtown?"` → routes to `foodie_agent`
- `"What concerts are happening this weekend in SF?"` → routes to `weekend_guide_agent`
- `"Plan me a full day trip to Napa Valley."` → routes to `day_trip_agent`

Notice the same router handles all three types of requests — you don't have to tell it which agent to use.

---

## Navigate Branches

```bash
git checkout 005-sequential            # next: sequential pipeline
git checkout 003-orchestrator          # back
```
