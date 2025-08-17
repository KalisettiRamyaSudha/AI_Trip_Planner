from utils.expense_calculator import Calculator
from typing import List
from pydantic import tool

class CalculatorTool:
    def __init__(self):
        self.calculator = Calculator()
        self.calculator_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        """
        Setup the tools for the calculator.
        
        Returns:
            List: A list of tool functions for expense calculations.
        """
        @tool
        def estimate_total_hotel_cost(price_per_night:str, total_days:float) -> float:
            """
            Estimate total hotel cost.
            
            Args:
                price_per_night (str): Price per night in string format.
                total_days (float): Total number of days.
            
            Returns:
                float: Total hotel cost.
            """
            price = float(price_per_night)
            return self.calculator.multiply(price, total_days)
        @tool
        def calculate_total_expense(*costs: float)->float:
            """ Calculate total expense for the trip"""
            return self.calculator.calculate_total(*costs)
        @tool
        def calculate_daily_expense_budget(total_cost: float, days: int)->float:
            """ Calculate daily budget"""
            return self.calculator.calculate_daily_budget(total_cost, days)
        
        return [estimate_total_hotel_cost, calculate_total_expense, calculate_daily_expense_budget]