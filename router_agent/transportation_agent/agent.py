from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

transportation_agent = Agent(
    name="transportation_agent",
    model="gemini-3.5-flash",
    tools=[google_search],
    instruction="""You are a navigation assistant. Given a destination, provide clear directions.
    The user wants to go to: {destination}.

    Analyze the user's full original query to find their starting point.
    Then, provide clear directions from that starting point to {destination}.
    """,
)
