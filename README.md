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

**Concept: Custom Skills (Tool Functions for File I/O)**

Any plain Python function becomes an agent tool. This branch shows tools that do real file work — reading a CSV, writing results back, and fetching exchange rates.

```python
def get_exchange_rates() -> dict:
    """Returns the currency exchange rate reference table."""
    ...

def clean_blank_rows() -> dict:
    """Removes hotel records missing name, city, or price from the CSV."""
    ...

def standardize_currencies(target_currency: str = "USD") -> dict:
    """Converts all hotel prices to the specified currency using exchange rates."""
    ...

root_agent = Agent(
    name="hotel_csv_cleaner",
    model="gemini-3.5-flash",
    tools=[get_exchange_rates, clean_blank_rows, standardize_currencies],
    instruction="You are a hotel data cleaning specialist...",
)
```

The data files live in `hotel_cleaner/data/`:
- `hotels_raw.csv` — 126 rows of hotel records with mixed currencies and missing values
- `exchange_rates.csv` — reference table for 14 currencies

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
| `city_explorer/` | ParallelAgent city guide (branch 007) |
| `hotel_cleaner/` | **New** — agent with file I/O skills: clean blanks + standardize currencies |

---

## Run an Agent

```bash
adk web hotel_cleaner
```

Open [http://localhost:8000](http://localhost:8000) in your browser.

## Things to Try (with `hotel_cleaner`)

- `"Show me the exchange rates."`
- `"Clean the hotel data."`
- `"Standardize all prices to EUR."`

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
| Loop | Iterates critic → refiner until quality is met or max rounds reached |
| Parallel | Fans out to multiple agents simultaneously, then aggregates |
| Skills (File I/O) | Tools that read and write files as part of a data workflow |

---

## Navigate Branches

```bash
git checkout 007-parallel-agent    # back
```
