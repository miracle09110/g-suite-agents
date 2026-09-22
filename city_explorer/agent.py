import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from google.adk.agents.llm_agent import Agent
from google.adk.agents.sequential_agent import SequentialAgent
from google.adk.agents.parallel_agent import ParallelAgent
from google.adk.tools import google_search

# ── Specialist agents ─────────────────────────────────────────────────────────
# Each runs independently and saves its result to a unique state key.

museum_finder_agent = Agent(
    name="museum_finder_agent",
    model="gemini-3.5-flash",
    tools=[google_search],
    instruction="""You are a museum and cultural attraction specialist.
    Search for the top museums, galleries, or cultural sites relevant to the user's city or topic.
    Return a short, formatted list of 3 recommendations with name, one-line description, and hours.
    """,
    output_key="museum_result",
)

concert_finder_agent = Agent(
    name="concert_finder_agent",
    model="gemini-3.5-flash",
    tools=[google_search],
    instruction="""You are a live events and entertainment specialist.
    Search for upcoming concerts, live music, festivals, or performance events relevant to the user's city or topic.
    Return a short, formatted list of 3 recommendations with event name, venue, and date/time.
    """,
    output_key="concert_result",
)

restaurant_finder_agent = Agent(
    name="restaurant_finder_agent",
    model="gemini-3.5-flash",
    tools=[google_search],
    instruction="""You are a food and dining specialist.
    Search for the best restaurants or dining experiences relevant to the user's city or topic.
    Return a short, formatted list of 3 recommendations with restaurant name, cuisine, and a one-line highlight.
    """,
    output_key="restaurant_result",
)

# ── Parallel workflow ─────────────────────────────────────────────────────────
# Runs all three finder agents simultaneously.
# Each writes to its own state key, so results never overwrite each other.

parallel_research_agent = ParallelAgent(
    name="parallel_research_agent",
    description="Simultaneously searches for museums, concerts, and restaurants.",
    sub_agents=[museum_finder_agent, concert_finder_agent, restaurant_finder_agent],
)

# ── Aggregator ────────────────────────────────────────────────────────────────
# Reads the three state keys and compiles a single cohesive response.

aggregator_agent = Agent(
    name="aggregator_agent",
    model="gemini-3.5-flash",
    instruction="""You are a travel guide writer. Compile the research below into one
    well-formatted city guide response for the user.

    Museums & Culture:
    {museum_result}

    Concerts & Events:
    {concert_result}

    Restaurants & Dining:
    {restaurant_result}

    Present all three sections clearly with headers. Keep it concise and easy to read.
    """,
)

# ── Root agent ────────────────────────────────────────────────────────────────
# Research in parallel first, then aggregate into one response.

root_agent = SequentialAgent(
    name="city_explorer",
    description="Researches museums, concerts, and restaurants in parallel, then compiles a city guide.",
    sub_agents=[parallel_research_agent, aggregator_agent],
)
