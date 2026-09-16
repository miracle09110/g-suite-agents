from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-3.5-flash',
    name='basic_chat_bot',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)
