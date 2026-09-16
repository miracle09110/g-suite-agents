from google.adk.agents.llm_agent import Agent
from google.adk.agents.sequential_agent import SequentialAgent
from google.adk.tools import google_search

# Dedicated instances for this pipeline — separate from the standalone agents
# in the router so each has exactly one parent (ADK requirement).
_foodie = Agent(
    name="pipeline_foodie",
    model="gemini-3.5-flash",
    tools=[google_search],
    instruction="""You are an expert food critic. Your goal is to find the best restaurant based on a user's request.

    When you recommend a place, you must output *only* the name of the establishment and nothing else.
    For example, if the best sushi is at 'Jin Sho', you should output only: Jin Sho
    """,
    output_key="destination"
)

_transport = Agent(
    name="pipeline_transport",
    model="gemini-3.5-flash",
    tools=[google_search],
    instruction="""You are a navigation assistant. Given a destination, provide clear directions.
    The user wants to go to: {destination}.

    Analyze the user's full original query to find their starting point.
    Then, provide clear directions from that starting point to {destination}.
    """,
)

find_and_navigate_agent = SequentialAgent(
    name="find_and_navigate_agent",
    sub_agents=[_foodie, _transport],
    description="A workflow that first finds a location and then provides directions to it."
)
