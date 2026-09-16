from google.adk.agents.llm_agent import Agent

db_agent = Agent(
    name="db_agent",
    model="gemini-3.6-flash",
    instruction=(
        "You are a database agent. When asked for data, return this mock JSON object: "
        "{'status': 'success', 'data': [{'name': 'The Grand Hotel', 'rating': 5, 'reviews': 450}, "
        "{'name': 'Seaside Inn', 'rating': 4, 'reviews': 620}]}"
    ),
)
