from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

foodie_agent = Agent(
    name="foodie_agent",
    model="gemini-3.5-flash",
    tools=[google_search],
    instruction="You are an expert food critic. Your goal is to find the absolute best food, restaurants, or culinary experiences based on a user's request. When you recommend a place, state its name clearly. For example: 'The best sushi is at **Jin Sho**.'",
)
