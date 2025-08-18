import requests
class WeatherForecastTool:
    def __init__(self, api_key:str):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5"

    def get_current_weather(self, place: str):
        """Fetch current weather data for a given place."""
        try:
            url = f"{self.base_url}/weather"
            params = {
                'q': place,
                'appid': self.api_key,
                'units': 'metric'
            }
            response = requests.get(url, params=params)
            return response.json() if response.status_code == 200 else {}
        except Exception as e:
            print(f"Error fetching current weather: {e}")
            raise e
        
    def get_forecast_weather(self, place: str):
        """Fetch weather forecast data for a given place."""
        try:
            url = f"{self.base_url}/forecast"
            params = {
                'q': place,
                'appid': self.api_key,
                "cnt": 10,  # Number of forecast data points
                'units': 'metric'
            }
            response = requests.get(url, params=params)
            return response.json() if response.status_code == 200 else {}
        except Exception as e:
            print(f"Error fetching weather forecast: {e}")
            raise e