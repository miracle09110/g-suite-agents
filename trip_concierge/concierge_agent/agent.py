from google.adk.agents.llm_agent import Agent
from google.adk.tools.agent_tool import AgentTool

from ..food_critic_agent import food_critic_agent

concierge_agent = Agent(
    name="concierge_agent",
    model="gemini-3.5-flash",
    instruction="You are a five-star hotel concierge. If the user asks for a restaurant recommendation, you MUST use the `food_critic_agent` tool. Present the opinion to the user politely.",
    tools=[AgentTool(agent=food_critic_agent)],
)
