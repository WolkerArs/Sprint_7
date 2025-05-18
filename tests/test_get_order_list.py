import allure

from methods.order_methods import OrderMethods

class TestGetOrderList:

    @allure.title('Проверка успешного получения списка заказов')
    def test_get_order_list_code_200(self):
        order_list = OrderMethods.get_list_of_orders()
        assert (order_list.status_code == 200
                and "orders" in order_list.json())