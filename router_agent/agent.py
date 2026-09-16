from google.adk.agents.llm_agent import Agent
from google.adk.agents.sequential_agent import SequentialAgent
from google.adk.tools import google_search

day_trip_agent = Agent(
    name="day_trip_agent",
    model="gemini-3.5-flash",
    description="Agent specialized in generating spontaneous full-day itineraries based on mood, interests, and budget.",
    instruction="""
    You are the "Spontaneous Day Trip" Generator 🚗 - a specialized AI assistant that creates engaging full-day itineraries.

    Your Mission:
    Transform a simple mood or interest into a complete day-trip adventure with real-time details, while respecting a budget.

    Guidelines:
    1. **Budget-Aware**: Pay close attention to budget hints like 'cheap', 'affordable', or 'splurge'. Use Google Search to find activities (free museums, parks, paid attractions) that match the user's budget.
    2. **Full-Day Structure**: Create morning, afternoon, and evening activities.
    3. **Real-Time Focus**: Search for current operating hours and special events.
    4. **Mood Matching**: Align suggestions with the requested mood (adventurous, relaxing, artsy, etc.).

    RETURN itinerary in MARKDOWN FORMAT with clear time blocks and specific venue names.
    """,
    tools=[google_search]
)

foodie_agent = Agent(
    name="foodie_agent",
    model="gemini-3.5-flash",
    tools=[google_search],
    instruction="You are an expert food critic. Your goal is to find the absolute best food, restaurants, or culinary experiences based on a user's request. When you recommend a place, state its name clearly. For example: 'The best sushi is at **Jin Sho**.'"
)

weekend_guide_agent = Agent(
    name="weekend_guide_agent",
    model="gemini-3.5-flash",
    tools=[google_search],
    instruction="You are a local events guide. Your task is to find interesting events, concerts, festivals, and activities happening on a specific weekend."
)

transportation_agent = Agent(
    name="transportation_agent",
    model="gemini-3.5-flash",
    tools=[google_search],
    instruction="You are a navigation assistant. Given a starting point and a destination, provide clear directions on how to get from the start to the end."
)

# Private pipeline agents — separate instances so each has exactly one parent.
# These are used only inside find_and_navigate_agent's sequential workflow.
_pipeline_foodie = Agent(
    name="pipeline_foodie",
    model="gemini-3.5-flash",
    tools=[google_search],
    instruction="""You are an expert food critic. Find the best restaurant based on the user's request.
    Output ONLY the name of the establishment — nothing else.
    Example: Jin Sho
    """,
    output_key="destination",
)

_pipeline_transport = Agent(
    name="pipeline_transport",
    model="gemini-3.5-flash",
    tools=[google_search],
    instruction="""You are a navigation assistant. The user wants to go to: {destination}.
    Analyze the user's original query to find their starting point, then provide clear directions.
    """,
)

# A SequentialAgent runs its sub_agents one after another, passing state between them.
# pipeline_foodie saves the restaurant name to state['destination'],
# which pipeline_transport then reads via the {destination} template.
find_and_navigate_agent = SequentialAgent(
    name="find_and_navigate_agent",
    description="A two-step workflow: first finds the best place, then provides directions to it.",
    sub_agents=[_pipeline_foodie, _pipeline_transport],
)

root_agent = Agent(
    name="router_agent",
    model="gemini-3.5-flash",
    sub_agents=[foodie_agent, weekend_guide_agent, day_trip_agent, transportation_agent, find_and_navigate_agent],
    instruction="""
    You are a request router. Your job is to analyze a user's query and decide which of the following agents is best suited to handle it.
    Forward the question to the right agent and return their response.

    Available Options:
    - 'foodie_agent': For queries *only* about food, restaurants, or eating.
    - 'weekend_guide_agent': For queries about events, concerts, or activities happening on a specific timeframe like a weekend.
    - 'transportation_agent': For queries about directions or getting from one place to another.
    - 'day_trip_agent': A general planner for any other day trip requests.
    - 'find_and_navigate_agent': For complex queries that ask to *first find a place* and *then get directions* to it.

    Only return the single, most appropriate option's name together with their response.
    """
)
