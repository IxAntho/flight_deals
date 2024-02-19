import requests
import os
from dotenv import load_dotenv

load_dotenv(".env")
flight_api_key: str = os.getenv("FLIGHT_API_KEY")
flight_search_endpoint: str = os.getenv("FLIGHT_LOCATION_ENDPOINT")

headers = {
    "Content-Type": "application/json",
    "apikey": flight_api_key,
}


class FlightSearch:

    def __init__(self):
        self.session = requests.Session()  # Use this if you're going to call the API many times

    def get_city_codes(self, cities):
        """Returns IATA codes for a list of city names in list format"""
        s = self.session
        codes = []
        for city in cities:
            parameters = {
                "term": f"{city}",
                "location_types": "city",
            }
            response = s.get(url=flight_search_endpoint, params=parameters, headers=headers)

            city_data = response.json()
            city_code = city_data["locations"][0]["code"]
            codes.append(city_code)
        return codes
