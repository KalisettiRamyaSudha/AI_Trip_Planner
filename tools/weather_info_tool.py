import os
from utils.weather_info import WeatherForecastTool
from langchain.tools import tool
from typing import List
from dotenv import load_dotenv

class WeatherInfoTool:
    def __init__(self):
        load_dotenv()
        self.api_key = os.environ.get("OPENWEATHERMAP_API_KEY")
        self.weather_service = WeatherForecastTool(self.api_key)
        self.weather_tool_list = self._setup_tools()

    def _setup_tools(self) -> List[tool]:
        """Setup the weather tools with the necessary parameters."""
        @tool
        def get_current_weather(self, city:str) -> str:
            """Get the current weather for a specified location."""
            weather_data = self.weather_service.get_current_weather(city)
            if weather_data:
                temp = weather_data.get('main',{}).get('temp', 'N/A')
                desc = weather_data.get('weather', [{}])[0].get('description', 'N/A')
                return f"The current temperature in {city} is {temp}°C with {desc}."
            return f"Could not retrieve weather for {city}"
        
        @tool
        def get_weather_forecast(self, city: str) -> str:
            """Get weather forecast for a city."""
            forecast_data = self.weather_service.get_forecast_weather(city)
            if forecast_data and 'list' in forecast_data:
                forecast_summary = []
                for i in range(len(forecast_data['list'])):
                    item = forecast_data['list'][i]
                    date = item['dt_txt'].split('')[0]
                    temp = item['main']['temp']
                    desc = item['weather'][0]['description'
                    forecast_summary.append(f"{date}: {temp}°C, {desc}")
                return f"Weather forecast for {city}:\n" + "\n".join(forecast_summary)
            return f"Could not fetch forecast for {city}"]

        return [get_current_weather, get_weather_forecast]