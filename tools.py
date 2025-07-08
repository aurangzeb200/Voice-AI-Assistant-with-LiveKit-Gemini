import logging
from livekit.agents import function_tool,RunContext
import requests
from langchain_community.tools import DuckDuckGoSearchRun

@function_tool
async def search(query: str, run_context: RunContext) -> str:
    """
    Search the web using DuckDuckGo and return the first result.
    """
    logging.info(f"Searching for: {query}")
    search_tool = DuckDuckGoSearchRun()
    results = search_tool.run(query)
    
    if results:
        first_result = results[0]
        logging.info(f"Search result found: {first_result}")
        return first_result
    else:
        logging.warning("No search results found.")
        return "No results found."
    

@function_tool
async def get_weather(city: str, run_context: RunContext) -> str:
    """
    Get the current weather for a given city.
    """
    try:
        response = response.get(
            url = f"https://wttr.in/{city}?format=3")
        if response.status_code == 200:
            weather_info = response.text.strip()
            logging.info(f"Weather info for {city}: {weather_info}")
            return weather_info
        
    except requests.RequestException as e:
        logging.error(f"Error {e} while fetching weather data for {city}")
        return "Could not retrieve weather information at this time."
        
    