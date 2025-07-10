import allure

from conftest import cleanup_courier
from methods.courier_methods import CourierMethods
from data import TextResponse

class TestCreateCourier:

    @allure.title('Проверка успешного создания курьера')
    def test_successful_create_courier_code_201(self, cleanup_courier):
        payload = cleanup_courier
        courier = CourierMethods.create_courier(payload)
        assert (courier.status_code == 201
                and courier.text == TextResponse.successful_create_courier)

    @allure.title('Проверка ошибки при создании курьера без логина')
    def test_create_courier_with_no_login_code_400(self, random_courier_data):
        payload = random_courier_data
        no_login_data = {
            'password': payload['password'],
            'firstName': payload['firstName']
        }
        courier = CourierMethods.create_courier(no_login_data)
        assert (courier.status_code == 400
                and courier.text == TextResponse.not_enough_data_create_courier)

    @allure.title('Проверка ошибки при создании курьера без пароля')
    def test_create_courier_with_no_password_code_400(self, random_courier_data):
        payload = random_courier_data
        no_password_data = {
            'login': payload['login'],
            'firstName': payload['firstName']
        }
        courier = CourierMethods.create_courier(no_password_data)
        assert (courier.status_code == 400
                and courier.text == TextResponse.not_enough_data_create_courier)

    @allure.title('Проверка ошибки при создании курьера без имени')
    def test_create_courier_with_no_name_code_400(self, random_courier_data):
        payload = random_courier_data
        no_name_data = {
            'login': payload['login'],
            'password': payload['password']
        }
        courier = CourierMethods.create_courier(no_name_data)
        assert (courier.status_code == 400
                and courier.text == TextResponse.not_enough_data_create_courier)

    @allure.title('Проверка ошибки при создании курьера с уже существующим логином')
    def test_create_courier_with_duplicate_login_code_409(self, new_courier):
        courier_body = new_courier[0]
        duplicate_courier = CourierMethods.create_courier(courier_body)
        assert (duplicate_courier.status_code == 409
                and duplicate_courier.text == TextResponse.duplicate_login_create_courier)