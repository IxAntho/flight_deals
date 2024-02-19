import requests
import os
from dotenv import load_dotenv

load_dotenv(".env")
get_endpoint: str = os.getenv("SHEETY_GET_ENDPOINT")
post_endpoint: str = os.getenv("SHEETY_POST_ENDPOINT")
put_endpoint: str = os.getenv("SHEETY_PUT_ENDPOINT")
header_auth = os.getenv("SHEETY_AUTH")

headers = {
    "Content-Type": "application/json",
    "Authorization": header_auth,
}


class DataManager:

    def __init__(self):
        self.session = requests.Session()


    def get_prices(self):
        s = self.session
        response = s.get(url=get_endpoint, headers=headers)
        data = response.json()
        print(data)
        cities = data["prices"]
        prices = []

        for city in cities:
            price = city["lowestPrice"]
            prices.append(price)

        return prices

    def get_cities(self):
        s = self.session
        response = s.get(url=get_endpoint, headers=headers)
        data = response.json()
        cities = data["prices"]
        names = []

        for city in cities:
            name = city["city"]
            names.append(name)

        return names

    def fill_codes(self, codes):
        s = self.session
        count = 2
        for code in codes:
            params = {
                "price": {
                    "iataCode": f"{code}",
                }
            }
            url = put_endpoint + f"{count}"
            r2 = s.put(url=url, json=params, headers=headers)
            count += 1
            print(code)
            print(r2.status_code)
