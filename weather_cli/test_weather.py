import unittest
from unittest.mock import patch
from weather import WeatherDashboard
from colorama import Fore, init

# Initialize colorama for colored output
init(autoreset=True)

class TestWeatherDashboard(unittest.TestCase):

    @patch("weather.requests.get")
    def test_valid_city(self, mock_get):
        """
        Test fetch_weather with a valid city and valid API key.
        Mocks a successful API response for a known city (London).
        """
        # Mocking a successful response for London
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "name": "London",  # City name in the response
            "main": {"temp": 15},  # Temperature
            "weather": [{"description": "clear sky"}]  # Weather condition
        }

        # Create WeatherDashboard instance and call fetch_weather
        dashboard = WeatherDashboard()
        result = dashboard.fetch_weather("London")

        # Validate that the result contains expected data
        self.assertIn("data", result)
        self.assertEqual(result["data"]["location"], "London")

    @patch("weather.requests.get")
    def test_invalid_api_key(self, mock_get):
        """
        Test fetch_weather with an invalid API key.
        Mocks an API response that returns 401 (Unauthorized) error.
        """
        # Mocking an invalid API key response
        mock_get.return_value.status_code = 401
        mock_get.return_value.json.return_value = {}

        # Create WeatherDashboard instance and call fetch_weather
        dashboard = WeatherDashboard()
        result = dashboard.fetch_weather("London")

        # Validate that the result contains an error message
        self.assertIn("error", result)
        self.assertIn("Invalid API key", result["error"])

    @patch("weather.requests.get")
    def test_invalid_city(self, mock_get):
        """
        Test fetch_weather with a city that doesn't exist.
        Mocks a 404 error response when the city is not found.
        """
        # Mocking a 404 error response for a non-existent city
        mock_get.return_value.status_code = 404
        mock_get.return_value.json.return_value = {}

        # Create WeatherDashboard instance and call fetch_weather
        dashboard = WeatherDashboard()
        result = dashboard.fetch_weather("FakeCity123")

        # Validate that the result contains an error message
        self.assertIn("error", result)
        self.assertIn("No such city", result["error"])

    @patch("weather.requests.get")
    def test_invalid_response_format(self, mock_get):
        """
        Test fetch_weather when the response format is invalid.
        Mocks a malformed response with unexpected fields in the JSON.
        """
        # Mocking a malformed response with unexpected fields
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "unexpected_field": "value"  # This is an invalid response format
        }

        # Create WeatherDashboard instance and call fetch_weather
        dashboard = WeatherDashboard()
        result = dashboard.fetch_weather("London")

        # Validate that the result contains an error message for unexpected format
        self.assertIn("error", result)
        self.assertIn("Unexpected response format", result["error"])

    # Adding custom colored output for the test results
    def addSuccess(self, test):
        """
        Called when a test is successful.
        Prints a success message in green.
        """
        super().addSuccess(test)
        print(Fore.GREEN + f"{test} passed successfully!")

    def addFailure(self, test, err):
        """
        Called when a test fails.
        Prints a failure message in red.
        """
        super().addFailure(test, err)
        print(Fore.RED + f"{test} failed!")

    def addError(self, test, err):
        """
        Called when a test encounters an error.
        Prints an error message in yellow.
        """
        super().addError(test, err)
        print(Fore.YELLOW + f"{test} encountered an error!")

if __name__ == "__main__":
    unittest.main(verbosity=2)
