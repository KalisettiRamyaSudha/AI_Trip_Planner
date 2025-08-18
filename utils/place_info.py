import os
import json
from langchain_tavily import TavilySearch
from langchain_google_community import GoogleSearchAPIWrapper, GooglePlacesTool

class GooglePlaceSearchTool:
    def __init__(self, api_key: str):
        self.places_wrapper = GooglePlacesAPIWrapper(gplaces_api_key=api_key)
        self.places_tool = GooglePlacesTool(api_wrapper=self.places_wrapper)

    def google_search_attraction(self, place:str)->dict:
        """
        Search for attractions in the specified place using GooglePlaces API.
        """
        try:
            results = self.places_tool.run(f"Top Tourist attraction places in and around {place}")
            return results
        except Exception as e:
            return {"error": str(e)}
        
    def google_search_restaurant(self, place:str)->dict:
        """
        Search for restaurants in the specified place using GooglePlaces API.
        """
        try:
            results = self.places_tool.run(f"Top Restaurants and eateries in {place}?")
            return results
        except Exception as e:
            return {"error": str(e)}
        
    def google_search_hotel(self, place:str)->dict:
        """
        Search for hotels in the specified place using GooglePlaces API.
        """
        try:
            results = self.places_tool.run(f"Top Hotels in {place}")
            return results
        except Exception as e:
            return {"error": str(e)}
        
    def google_search_activity(self, place:str)->dict:
        """
        Search for activities in the specified place using GooglePlaces API.
        """
        try:
            results = self.places_tool.run(f"Top Activities to do in {place}")
            return results
        except Exception as e:
            return {"error": str(e)}
        
    def google_search_transportation(self, place:str)->dict:
        """
        Search for transportation options in the specified place using GooglePlaces API.
        """
        try:
            results = self.places_tool.run(f"What are different Transportation options available in {place}")
            return results
        except Exception as e:
            return {"error": str(e)}
        
class TavilyPlaceSearchTool:
    def __init__(self)
        pass
    def tavily_search_attraction(self, place:str)->dict:
        """
        Search for attractions in the specified place using Tavily API.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result=tavily_tool.invoke({"query":f"Top Tourist attraction places in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result
    def tavily_search_restaurant(self, place:str)->dict:
        """
        Search for restaurants in the specified place using Tavily API.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result=tavily_tool.invoke({"query":f"Top 10 Restaurants and eateries in {place}?"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        
        return result
    def tavily_search_hotel(self, place:str)->dict:
        """ Search for hotels in the specified place using Tavily API.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result=tavily_tool.invoke({"query":f"What are some good Hotels for staying in {place}?"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        
        return result
    def tavily_search_activity(self, place:str)->dict:
        """ Search for activities in the specified place using Tavily API.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result=tavily_tool.invoke({"query":f"What are some fun Activities to do in {place}?"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        
        return result
    def tavily_search_transportation(self, place:str)->dict:
        """ Search for transportation options in the specified place using Tavily API.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result=tavily_tool.invoke({"query":f"What are different Transportation options available in {place}?"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        
        return result


