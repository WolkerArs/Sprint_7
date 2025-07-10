import allure

from methods.courier_methods import CourierMethods
from data import TextResponse

class TestLoginCourier:

    @allure.title('Проверка успешной авторизации')
    def test_successful_login_courier_code_200(self, new_courier):
        courier_body = new_courier[0]
        courier = CourierMethods.login_courier(courier_body)
        assert (courier.status_code == 200
                and courier.json()["id"] == CourierMethods.get_courier_id(courier_body))

    @allure.title('Проверка ошибки при авторизации без логина')
    def test_login_courier_no_login_code_400(self, new_courier):
        courier_body = {'password': new_courier[0]['password']}
        courier = CourierMethods.login_courier(courier_body)
        assert (courier.status_code == 400
                and courier.text == TextResponse.not_enough_data_login_courier)

    @allure.title('Проверка ошибки при авторизации без пароля')
    def test_login_courier_no_password_code_400(self, new_courier):
        courier_body = {'login': new_courier[0]['login']}
        courier = CourierMethods.login_courier(courier_body)
        assert (courier.status_code == 400
                and courier.text == TextResponse.not_enough_data_login_courier)

    @allure.title('Проверка ошибки при авторизации с несуществующими логином-паролем')
    def test_login_courier_not_existing_courier_code_404(self, random_login_pass):
        courier = CourierMethods.login_courier(random_login_pass)
        assert (courier.status_code == 404
                and courier.text == TextResponse.not_existing_courier_login_courier)