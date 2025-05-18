import requests
from data import Url

class OrderMethods:

    @staticmethod
    def create_order(body):
        return requests.post(Url.orders_url, data=body)

    @staticmethod
    def get_list_of_orders():
        return requests.get(Url.orders_url)

    @staticmethod
    def cancel_order(body):
        return requests.put(Url.cancel_orders_url, data=body)