import pytest

from courier_methods import CourierMethods
from helpers import Helpers


@pytest.fixture
def courier():
    courier_data = Helpers.generate_courier_data()

    CourierMethods.create_courier(courier_data)

    login_response = CourierMethods.login_courier({
        "login": courier_data["login"],
        "password": courier_data["password"]
    })

    courier_id = login_response.json()["id"]

    yield courier_data

    CourierMethods.delete_courier(courier_id)


@pytest.fixture
def courier_data():
    data = Helpers.generate_courier_data()

    login = data["login"]
    password = data["password"]

    yield data

    login_response = CourierMethods.login_courier({
        "login": login,
        "password": password
    })

    if login_response.status_code == 200:
        courier_id = login_response.json()["id"]
        CourierMethods.delete_courier(courier_id)