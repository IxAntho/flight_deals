import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv(".env")
flight_api_key: str = os.getenv("FLIGHT_API_KEY")
flight_search_endpoint: str = os.getenv("FLIGHT_SEARCH_ENDPOINT")

headers = {
    "Content-Type": "application/json",
    "apikey": flight_api_key,
}


class FlightData:

    def __init__(self):
        self.session = requests.Session()
        self.today = datetime.now()
        self.tomorrow = (self.today + timedelta(days=1)).strftime("%d/%m/%Y")
        self.six_months = (self.today + timedelta(days=180)).strftime("%d/%m/%Y")

    def get_deals(self, codes):
        s = self.session
        best_deals = []
        for code in codes:
            parameters = {
                "fly_from": "BWI",
                "fly_to": f"{code}",
                "date_from": f"{self.tomorrow}",
                "date_to": f"{self.six_months}",
            }
            response = s.get(url=flight_search_endpoint, params=parameters, headers=headers)
            data = response.json()
            price = data["data"][0]["price"]
            departure = data["data"][0]["local_departure"].split("T")[0]
            airport_code = data["data"][0]["flyTo"]
            city_name = data["data"][0]["cityTo"]
            deal = {
                "code": code,
                "price": price,
                "departure": departure,
                "IATA code": airport_code,
                "city":city_name,
            }
            best_deals.append(deal)
        return best_deals
