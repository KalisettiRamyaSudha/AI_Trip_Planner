import requests

class CurrencyConverter:
    def __init__(self, api_key: str):

        self.base_url = "https://open.er-api.com/v6/latest/"

    def convert(self, amount:float, from_currency:str, to_currency:str):
        """
        Convert amount from one currency to another.
        
        Args:
            amount (float): Amount to convert.
            from_currency (str): Currency code to convert from.
            to_currency (str): Currency code to convert to.
        
        Returns:
            float: Converted amount in the target currency.
        """
        url = f"{self.base_url}/{from_currency}"
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception("Error fetching currency data.API call failed:", response.json())
        rates = response.json()["conversion_rates"]
        if to_currency not in rates:
            raise ValueError(f"Currency {to_currency} not found in conversion rates.")

        return amount * rates[to_currency]