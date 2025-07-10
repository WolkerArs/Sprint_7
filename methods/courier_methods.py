import allure
import requests
from data import Url

class CourierMethods:

    @staticmethod
    @allure.step(f'Создать курьера через POST-запрос на {Url.courier_url}')
    def create_courier(body):
        return requests.post(Url.courier_url, data=body)

    @staticmethod
    @allure.step(f'Авторизоваться курьером через POST-запрос на {Url.login_courier_url}')
    def login_courier(body):
        return requests.post(Url.login_courier_url, data=body)

    @staticmethod
    @allure.step(f'Удалить курьера через DELETE-запрос на {Url.courier_url}')
    def delete_courier(id):
        return requests.delete(f'{Url.courier_url}/{id}')

    @staticmethod
    @allure.step('Получить ID курьера')
    def get_courier_id(body):
        id = CourierMethods.login_courier(body).json()['id']
        return id