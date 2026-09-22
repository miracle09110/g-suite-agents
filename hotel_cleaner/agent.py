from google.adk.agents.llm_agent import Agent

from .skills import get_exchange_rates, clean_blank_rows, standardize_currencies

root_agent = Agent(
    name="hotel_csv_cleaner",
    model="gemini-3.5-flash",
    tools=[get_exchange_rates, clean_blank_rows, standardize_currencies],
    instruction="""You are a hotel data cleaning specialist.
    You have three skills available:

    1. get_exchange_rates     — view the currency conversion reference table
    2. clean_blank_rows       — remove hotel records missing name, city, or price
    3. standardize_currencies — convert all prices to one currency (default: USD)

    The raw hotel data is at: hotel_cleaner/data/hotels_raw.csv

    Typical workflow when the user asks to clean the dataset:
      Step 1 → clean_blank_rows  (removes incomplete records)
      Step 2 → standardize_currencies  (converts prices to USD or requested currency)

    Always report what was done and how many rows were affected.
    """,
)
