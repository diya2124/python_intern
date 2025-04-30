import requests
import json
import time
from datetime import datetime
from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class WeatherDashboard:
    def __init__(self):
        self.api_key = os.getenv("WEATHER_API_KEY")
        self.history_file = "history.json"
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
        self.cache = {}
        self.cache_duration = 300  # 5 minutes

    def fetch_weather(self, city):
        city_lower = city.lower()

        # Return cached data if it's recent
        if city_lower in self.cache:
            cached_data, timestamp = self.cache[city_lower]
            if time.time() - timestamp < self.cache_duration:
                return cached_data

        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }

        try:
            response = requests.get(self.base_url, params=params)
            if response.status_code == 404:
                return {"error": f"No such city found: {city}"}
            response.raise_for_status()
            data = response.json()

            weather_info = {
                "city": city,
                "data": {
                    "location": data.get("name"),
                    "temperature": data["main"]["temp"],
                    "condition": data["weather"][0]["description"],
                    "timestamp": datetime.now().isoformat()
                }
            }

            # Cache the result
            self.cache[city_lower] = (weather_info, time.time())
            return weather_info

        except requests.exceptions.RequestException as e:
            return {"error": f"Request failed: {e}"}

    def save_to_history(self, weather_data):
        path = Path(self.history_file)
        if path.exists():
            with open(path, "r") as f:
                history = json.load(f)
        else:
            history = []

        history.append(weather_data)
        with open(path, "w") as f:
            json.dump(history, f, indent=2)

    def load_history(self):
        path = Path(self.history_file)
        if path.exists():
            with open(path, "r") as f:
                return json.load(f)
        return []

    def display_weather(self, weather_data):
        if "error" in weather_data:
            print(f"❌ Error: {weather_data['error']}")
        else:
            data = weather_data["data"]
            print(f"\nWeather in {data['location']}:")
            print(f"Temperature: {data['temperature']}°C")
            print(f"Condition: {data['condition'].capitalize()}")
            print(f"Timestamp: {data['timestamp']}\n")

if __name__ == "__main__":
    city = input("Enter city name: ").strip()

    dashboard = WeatherDashboard()
    weather = dashboard.fetch_weather(city)
    dashboard.display_weather(weather)

    if "error" not in weather:
        dashboard.save_to_history(weather)
