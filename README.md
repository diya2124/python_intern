# python_intern
# Markdown Analyzer Tool



A simple Python tool to analyze `.md` (Markdown) files. It provides useful metrics and checks for broken links.

## Features

-  Word count
-  Heading count
-  Link count
-  Image count

## Requirements

- Python 3.7

#### Getting a GitHub Token
1. Go to GitHub Profile → Settings → Developer settings
2. Navigate to Personal access tokens → Tokens (classic)
3. Generate new token (classic)
4. Set appropriate permissions and expiration
5. Save the token securely

#### Repository Setup
Clone using either:
bash
git clone https://github.com/diya2124/python_intern.git








#  Weather Dashboard CLI

A simple Python-based command-line tool that fetches and displays current weather conditions using the OpenWeatherMap API. It also stores your query history locally.

---

## Features

-->Fetch current weather by entering a city name.
-->Displays temperature, condition, and timestamp.
-->Handles missing or invalid city names.
-->Stores fetched weather data in a local JSON file (history.json).
-->Caches results to reduce API calls.
-->Reads the API key securely from a .env file.

# To run
python weather.py

# Sample output
 Enter city name: London

Weather in London:
Temperature: 12.34°C
Condition: Clear sky
Timestamp: 2025-04-30T15:30:10

# Not found
  Error: No such city found: UnknownCity

