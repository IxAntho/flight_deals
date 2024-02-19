import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv(".env")
api_key: str = os.getenv("TWILIO_API_KEY")
account_sid: str = os.getenv("TWILIO_ACCOUNT_SID")
auth_token: str = os.getenv("TWILIO_AUTH_TOKEN")
my_phone: str = os.getenv("PHONE_SENDER")
other_phone: str = os.getenv("PHONE_RECEIVER")


class NotificationManager:

    def __init__(self, deals):
        self.session = requests.Session()
        self.message = self.create_message(deals)

    def create_message(self, deals):
        message = ""
        for data in deals:
            deal = f"\nLow price alert! only ${data["price"]}, to fly from Washington DC - BWI to {data["city"]}-{data["IATA code"]} on {data["departure"]}\n"
            message += deal

        return message

    def send_message(self):
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_=my_phone,
            body=self.message,
            to=other_phone,
        )
        print(message)
