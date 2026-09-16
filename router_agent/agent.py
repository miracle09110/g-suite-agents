from google.adk.agents.llm_agent import Agent

from .day_trip_agent import day_trip_agent
from .foodie_agent import foodie_agent
from .weekend_guide_agent import weekend_guide_agent
from .find_and_navigate_agent import find_and_navigate_agent

root_agent = Agent(
    name="router_agent",
    model="gemini-3.5-flash",
    sub_agents=[foodie_agent, weekend_guide_agent, day_trip_agent, find_and_navigate_agent],
    instruction="""
    You are a request router. Your job is to analyze a user's query and decide which of the following agents or workflows is best suited to handle it.
    Forward the question to the right agent and return their response.

    Available Options:
    - 'foodie_agent': For queries *only* about food, restaurants, or eating.
    - 'weekend_guide_agent': For queries about events, concerts, or activities happening on a specific timeframe like a weekend.
    - 'day_trip_agent': A general planner for any other day trip requests.
    - 'find_and_navigate_agent': Use this for complex queries that ask to *first find a place* and *then get directions* to it.

    Only return the single, most appropriate option's name together with their response.
    """
)
