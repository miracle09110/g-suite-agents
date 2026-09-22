import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from google.adk.agents.llm_agent import Agent
from google.adk.agents.sequential_agent import SequentialAgent
from google.adk.agents.loop_agent import LoopAgent
from google.adk.tools.exit_loop_tool import exit_loop

# Step 1: Draft the initial plan from the user's goal
planner_agent = Agent(
    name="planner_agent",
    model="gemini-3.5-flash",
    instruction="""You are a strategic planner. Given the user's goal or topic,
    create a clear, structured plan with 3-5 actionable steps.

    Format your output as a numbered list. Be specific and practical.
    Output ONLY the plan — no preamble, no explanation.
    """,
    output_key="current_plan",
)

# Step 2a: Critique the current plan (runs inside the loop)
# Calls exit_loop if the plan is already strong enough to stop early.
critic_agent = Agent(
    name="critic_agent",
    model="gemini-3.5-flash",
    tools=[exit_loop],
    instruction="""You are a critical reviewer. Evaluate this plan:

{current_plan}

If the plan is clear, complete, and actionable with no significant gaps, call exit_loop to stop.

Otherwise, list 2-3 specific weaknesses or missing elements that must be addressed.
Output ONLY the critique — no preamble.
""",
    output_key="critique",
)

# Step 2b: Refine the plan using the critique (runs inside the loop)
refiner_agent = Agent(
    name="refiner_agent",
    model="gemini-3.5-flash",
    instruction="""You are a plan improvement specialist.

Current plan:
{current_plan}

Critique:
{critique}

Rewrite the plan to address every point in the critique while keeping what already works.
Output ONLY the improved numbered plan — no preamble, no explanation.
""",
    output_key="current_plan",
)

# Runs critic → refiner in a loop, up to 3 times.
# The loop stops early if critic_agent calls exit_loop.
refinement_loop = LoopAgent(
    name="refinement_loop",
    sub_agents=[critic_agent, refiner_agent],
    max_iterations=3,
)

# Root: plan first, then refine in a loop
root_agent = SequentialAgent(
    name="loop_planner",
    description="Drafts a plan then iteratively refines it through critic-refiner cycles (max 3 rounds).",
    sub_agents=[planner_agent, refinement_loop],
)
