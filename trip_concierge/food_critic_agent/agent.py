from google.adk.agents.llm_agent import Agent

food_critic_agent = Agent(
    name="food_critic_agent",
    model="gemini-3.5-flash",
    instruction="You are a snobby but brilliant food critic. You ONLY respond with a single, witty restaurant suggestion near the provided location.",
)
