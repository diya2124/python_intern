import requests
import json
import time
from datetime import datetime

# Cache duration set to 5 minutes (300 seconds)
CACHE_DURATION = 300  # seconds (5 minutes)
cache = {}  # Global cache to store weather data

class WeatherAPIHandler:
    """
    A class to interact with the OpenWeatherMap API to fetch weather data.
    
    It includes caching functionality to avoid fetching the same data repeatedly
    within a short time frame (5 minutes by default). The data is cached locally
    in memory to improve efficiency and minimize API calls.
    """
    
    def __init__(self, api_key):
        """
        Initializes the WeatherAPIHandler with the given API key.
        
        Args:
            api_key (str): The API key used to authenticate with the OpenWeatherMap API.
        """
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"  # Base URL for the weather API

    def get_weather(self, city):
        """
        Fetches weather data for a given city, either from cache or by making an API call.
        
        If the data is already cached and the cache is still valid (within 5 minutes),
        the cached data will be returned. Otherwise, a fresh request is made to the OpenWeatherMap API.
        
        Args:
            city (str): The name of the city for which to fetch weather data.
        
        Returns:
            dict: A dictionary containing weather data or an error message.
        """
        city_lower = city.lower()  # Convert city name to lowercase to ensure case-insensitive cache lookup

        # Check if the data is cached and still valid
        if city_lower in cache:
            cached_data, timestamp = cache[city_lower]
            if time.time() - timestamp < CACHE_DURATION:
                # If the cached data is still valid (not older than CACHE_DURATION), return it
                return cached_data

        # If no valid cache, make an API request
        params = {
            "q": city,  # City name
            "appid": self.api_key,  # API key
            "units": "metric"  # Units for temperature (Celsius)
        }

        try:
            # Make the GET request to the OpenWeatherMap API
            response = requests.get(self.base_url, params=params)
            # Raise an HTTPError if the response code indicates an error
            response.raise_for_status()
            data = response.json()  # Parse the JSON response

            # Extract relevant weather information from the response
            weather_info = {
                "city": data["name"],  # City name
                "temperature": data["main"]["temp"],  # Temperature in Celsius
                "description": data["weather"][0]["description"],  # Weather description (e.g., "clear sky")
                "humidity": data["main"]["humidity"],  # Humidity percentage
                "timestamp": datetime.now().isoformat()  # Timestamp of the data retrieval
            }

            # Cache the weather data with the current timestamp
            cache[city_lower] = (weather_info, time.time())

            return weather_info

        except requests.exceptions.HTTPError as e:
            # Handle HTTP errors (e.g., invalid city name or API issues)
            return {"error": f"HTTP error: {e}"}
        except requests.exceptions.ConnectionError:
            # Handle connection errors (e.g., network issues)
            return {"error": "Network connection error"}
        except requests.exceptions.Timeout:
            # Handle timeout errors
            return {"error": "Request timed out"}
        except requests.exceptions.RequestException as e:
            # Handle any other request exceptions
            return {"error": f"API request failed: {e}"}
        except KeyError:
            # Handle unexpected API response structure (e.g., missing fields)
            return {"error": "Unexpected API response structure"}
