import requests
from data import Url

class CourierMethods:

    @staticmethod
    def create_courier(body):
        return requests.post(Url.courier_url, data=body)

    @staticmethod
    def login_courier(body):
        return requests.post(Url.login_courier_url, data=body)

    @staticmethod
    def delete_courier(id):
        return requests.delete(f'{Url.courier_url}/{id}')

    @staticmethod
    def get_courier_id(body):
        id = CourierMethods.login_courier(body).json()['id']
        return id