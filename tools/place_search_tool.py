import os
from utils.place_info import GooglePlaceSearchTool, TavilyPlaceSearchTool
from typing import List
from langchain.tools import tool
from dotenv import load_dotenv

class PlaceSearchTool:
    def __init__(self):
        load_dotenv()
        self.google_api_key = os.environ.get("GPLACES_API_KEY")
        self.google_places_search = GooglePlaceSearchTool(self.google_api_key)
        self.tavily_search = TavilyPlaceSearchTool()
        self.place_search_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        """Setup the list of place search tools."""
        @tool
        def search_attractions(place:str)->str:
            """Search for attractions in a place"""
            try:
                attraction_result = self.google_places_search.google_search_attractions(place)
                if attraction_result:
                    return f"Following are the attractions of {place} as suggested by Google:\n{attraction_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_attractions(place)
                return f"Google cannot find the details due to {e}. \nFollowing are the attractions of {place}: {tavily_result}"  
                ## Fallback search using tavily in case google places fail

        @tool
        def search_restaurants(place:str)->str:
            """Search for restaurants in a place"""
            try:
                restaurant_result = self.google_places_search.google_search_restaurants(place)
                if restaurant_result:
                    return f"Following are the restaurants of {place} as suggested by Google:\n{restaurant_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_restaurants(place)
                return f"Google cannot find the details due to {e}. \nFollowing are the restaurants of {place}: {tavily_result}"  
                ## Fallback search using tavily in case google places fail

        @tool
        def search_hotels(place:str)->str:
            """Search for hotels in a place"""
            try:
                hotel_result = self.google_places_search.google_search_hotels(place)
                if hotel_result:
                    return f"Following are the hotels of {place} as suggested by Google:\n{hotel_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_hotels(place)
                return f"Google cannot find the details due to {e}. \nFollowing are the hotels of {place}: {tavily_result}"  
                ## Fallback search using tavily in case google places fail

        @tool
        def search_activities(place:str)->str:
            """Search for activities in a place"""
            try:
                activity_result = self.google_places_search.google_search_activities(place)
                if activity_result:
                    return f"Following are the activities of {place} as suggested by Google:\n{activity_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_activities(place)
                return f"Google cannot find the details due to {e}. \nFollowing are the activities of {place}: {tavily_result}"  
                ## Fallback search using tavily in case google places fail

        @tool
        def search_transportation(place:str)->str:
            """Search for transportation in a place"""
            try:
                transportation_result = self.google_places_search.google_search_transportation(place)
                if transportation_result:
                    return f"Following are the transportation options of {place} as suggested by Google:\n{transportation_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_transportation(place)
                return f"Google cannot find the details due to {e}. \nFollowing are the transportation options of {place}: {tavily_result}"  
                ## Fallback search using tavily in case google places fail

        return [
            search_attractions,
            search_restaurants,
            search_hotels,
            search_activities,
            search_transportation
        ]

            