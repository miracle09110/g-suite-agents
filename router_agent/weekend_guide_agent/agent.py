from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

weekend_guide_agent = Agent(
    name="weekend_guide_agent",
    model="gemini-3.5-flash",
    tools=[google_search],
    instruction="You are a local events guide. Your task is to find interesting events, concerts, festivals, and activities happening on a specific weekend."
)
