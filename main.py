# This file will need to use the DataManager, FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data = DataManager()
flight_searcher = FlightSearch()
flight_deal = FlightData()

cities = data.get_cities()
lowest_prices = data.get_prices()
codes = flight_searcher.get_city_codes(cities)
data.fill_codes(codes)
deals = flight_deal.get_deals(codes)
notification = NotificationManager(deals)
notification.send_message()


