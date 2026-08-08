import pytest

from courier_methods import CourierMethods
from helpers import Helpers


@pytest.fixture
def courier():
    courier_data = Helpers.generate_courier_data()

    create_response = CourierMethods.create_courier(courier_data)
    assert create_response.status_code == 201

    login_response = CourierMethods.login_courier({
        "login": courier_data["login"],
        "password": courier_data["password"]
    })
    courier_id = login_response.json()["id"]

    yield courier_data

    CourierMethods.delete_courier(courier_id)