import allure
import requests
from data import Url

class OrderMethods:

    @staticmethod
    @allure.step(f'Создать заказ через POST-запрос на {Url.orders_url}')
    def create_order(body):
        return requests.post(Url.orders_url, data=body)

    @staticmethod
    @allure.step(f'Получить список заказов через GET-запрос на {Url.orders_url}')
    def get_list_of_orders():
        return requests.get(Url.orders_url)

    @staticmethod
    @allure.step(f'Отменить заказ через PUT-запрос на {Url.cancel_orders_url}')
    def cancel_order(body):
        return requests.put(Url.cancel_orders_url, data=body)