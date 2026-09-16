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

**Concept: The Basic Agent**

An `Agent` is just an LLM given a name, a model, and instructions. That's it.

```python
from google.adk.agents import Agent

root_agent = Agent(
    model='gemini-2.0-flash',
    name='root_agent',
    instruction='Answer user questions to the best of your knowledge',
)
```

No tools. No memory. Just the model responding to your prompts. Every pattern you'll learn in the later branches starts here.

---

## Run This Agent

```bash
adk web basic_chat_bot
```

Open [http://localhost:8000](http://localhost:8000) in your browser.

## Things to Try

- `"What is the capital of France?"`
- `"Explain machine learning in one sentence."`
- `"Write a haiku about coffee."`

The agent answers from the model's training data only — it has no internet access yet. You'll add that in the next branch.

---

## Move to the Next Branch

```bash
git checkout 001-agent-with-tool
```

Your `.env` file is not tracked by git, so it stays in place when you switch branches.
