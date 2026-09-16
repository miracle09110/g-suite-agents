from google.adk.agents.sequential_agent import SequentialAgent

from ..foodie_agent import foodie_agent
from ..transportation_agent import transportation_agent

find_and_navigate_agent = SequentialAgent(
    name="find_and_navigate_agent",
    sub_agents=[foodie_agent, transportation_agent],
    description="A workflow that first finds a location and then provides directions to it."
)
