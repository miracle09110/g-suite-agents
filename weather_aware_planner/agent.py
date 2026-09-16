import requests
from google.adk.agents.llm_agent import Agent

LOCATION_COORDINATES = {
    "manila": (14.5995, 120.9842),
    "quezon city": (14.6760, 121.0437),
    "caloocan": (14.6499, 120.9803),
    "las pinas": (14.4453, 120.9830),
    "las piñas": (14.4453, 120.9830),
    "makati": (14.5547, 121.0244),
    "malabon": (14.6625, 120.9577),
    "mandaluyong": (14.5794, 121.0359),
    "marikina": (14.6507, 121.1029),
    "muntinlupa": (14.4081, 121.0415),
    "navotas": (14.6684, 120.9428),
    "paranaque": (14.4793, 121.0198),
    "parañaque": (14.4793, 121.0198),
    "pasay": (14.5378, 120.9932),
    "pasig": (14.5764, 121.0851),
    "pateros": (14.5440, 121.0680),
    "san juan": (14.6019, 121.0355),
    "taguig": (14.5243, 121.0792),
    "bgc": (14.5490, 121.0534),
    "valenzuela": (14.6943, 120.9832),
}

WMO_WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
    45: "Foggy", 48: "Icy fog",
    51: "Light drizzle", 53: "Moderate drizzle", 55: "Dense drizzle",
    61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
    80: "Slight showers", 81: "Moderate showers", 82: "Violent showers",
    95: "Thunderstorm", 96: "Thunderstorm with hail", 99: "Thunderstorm with heavy hail",
}

def get_live_weather_forecast(location: str) -> dict:
    """Gets the current, real-time weather forecast for a city in Metro Manila.

    Args:
        location: The city name, e.g., "Makati", "BGC", or "Quezon City".

    Returns:
        A dictionary containing the temperature, weather condition, and wind speed.
    """
    print(f"🛠️ TOOL CALLED: get_live_weather_forecast(location='{location}')")

    normalized = location.lower().replace("ñ", "n")
    coords = None
    for key, val in LOCATION_COORDINATES.items():
        if key in normalized or normalized in key:
            coords = val
            break

    if not coords:
        cities = ", ".join(k.title() for k in LOCATION_COORDINATES if k != "bgc")
        return {
            "status": "error",
            "message": f"Location '{location}' not found. Available cities: {cities}."
        }

    lat, lon = coords
    try:
        url = (
            f"https://api.open-meteo.com/v1/forecast"
            f"?latitude={lat}&longitude={lon}"
            f"&current_weather=true"
            f"&timezone=Asia%2FManila"
        )
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()["current_weather"]

        condition = WMO_WEATHER_CODES.get(data["weathercode"], "Unknown conditions")
        return {
            "status": "success",
            "location": location.title(),
            "temperature": f"{data['temperature']}°C",
            "condition": condition,
            "wind_speed": f"{data['windspeed']} km/h",
        }
    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": f"Weather API request failed: {e}"}


root_agent = Agent(
    name="weather_aware_planner",
    model="gemini-3.6-flash",
    description="A trip planner that checks real-time Metro Manila weather before making suggestions.",
    instruction=(
        "You are a local trip planner for Metro Manila, Philippines. "
        "Before suggesting any outdoor activities, you MUST use the `get_live_weather_forecast` tool "
        "to check current conditions for the requested city. "
        "Incorporate the live weather — temperature, condition, and wind — into your recommendation."
    ),
    tools=[get_live_weather_forecast]
)
