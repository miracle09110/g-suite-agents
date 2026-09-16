from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

foodie_agent = Agent(
    name="foodie_agent",
    model="gemini-3.6-flash",
    tools=[google_search],
    instruction="""You are an expert food critic. Your goal is to find the best restaurant based on a user's request.

    When you recommend a place, you must output *only* the name of the establishment and nothing else.
    For example, if the best sushi is at 'Jin Sho', you should output only: Jin Sho
    """,
    output_key="destination"  # ADK will save the agent's final response to state['destination']
)
