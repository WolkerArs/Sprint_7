import json

import allure
import pytest

from methods.order_methods import OrderMethods
from data import OrderData

class TestCreateOrder:

    @allure.title('Проверка успешного создания заказа')
    @pytest.mark.parametrize('order_body', OrderData.order_data)
    def test_successful_create_order(self, order_body, cleanup_order):
        json_order = json.dumps(order_body)
        new_order = OrderMethods.create_order(json_order)
        order_track = new_order.json()['track']
        cleanup_order(order_track)
        assert new_order.status_code == 201 and "track" in new_order.json()
