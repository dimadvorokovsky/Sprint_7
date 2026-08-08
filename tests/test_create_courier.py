import allure
import pytest

from courier_methods import CourierMethods
from helpers import Helpers


@allure.suite("Создание курьера")
class TestCreateCourier:

    @allure.title("Курьера можно успешно создать")
    def test_create_courier_with_valid_data_returns_201_and_true(self):
        courier_data = Helpers.generate_courier_data()
        response = CourierMethods.create_courier(courier_data)

        try:
            assert response.status_code == 201
            assert response.json() == {"ok": True}
        finally:
            login_response = CourierMethods.login_courier({
                "login": courier_data["login"],
                "password": courier_data["password"]
            })

            if login_response.status_code == 200:
                courier_id = login_response.json()["id"]
                CourierMethods.delete_courier(courier_id)

    @allure.title("Нельзя создать двух курьеров с одинаковым логином")
    def test_create_two_identical_couriers_returns_error(self):
        courier_data = Helpers.generate_courier_data()
        first_response = CourierMethods.create_courier(courier_data)

        try:
            second_response = CourierMethods.create_courier(courier_data)

            assert first_response.status_code == 201
            assert second_response.status_code in (400, 409)
            assert "message" in second_response.json()
        finally:
            login_response = CourierMethods.login_courier({
                "login": courier_data["login"],
                "password": courier_data["password"]
            })

            if login_response.status_code == 200:
                courier_id = login_response.json()["id"]
                CourierMethods.delete_courier(courier_id)

    @allure.title("Без обязательного поля курьер не создаётся")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_without_required_field_returns_error(
        self,
        missing_field
    ):
        courier_data = Helpers.generate_courier_data()
        courier_data.pop(missing_field)

        response = CourierMethods.create_courier(courier_data)

        assert response.status_code == 400
        assert response.json()["message"] == (
            "Недостаточно данных для создания учетной записи"
        )