import pytest

from methods.courier_methods import CourierMethods
from methods.order_methods import OrderMethods
from generators import register_new_courier_and_return_login_password, generate_courier_data


@pytest.fixture
def new_courier():
    data_courier, status_code, response_text = register_new_courier_and_return_login_password()
    courier_body = {
                    'login': data_courier[0],
                    'password': data_courier[1]
                    }
    yield [courier_body, status_code, response_text]
    courier_id = CourierMethods.get_courier_id(courier_body)
    CourierMethods.delete_courier(courier_id)

@pytest.fixture
def random_login_pass():
    courier = generate_courier_data()
    courier_body = {
                    'login': courier['login'],
                    'password': courier['password']
                    }
    yield courier_body

@pytest.fixture
def random_courier_data():
    courier_body = generate_courier_data()
    yield courier_body

@pytest.fixture
def cleanup_courier():
    courier_body = generate_courier_data()
    yield courier_body

    courier_id = CourierMethods.get_courier_id(courier_body)
    CourierMethods.delete_courier(courier_id)


@pytest.fixture
def cleanup_order():
        order_tracks = []
        def register_track(track):
            order_tracks.append(track)

        yield register_track

        for track in order_tracks:
            track_body = {"track": track}
            OrderMethods.cancel_order(track_body)

