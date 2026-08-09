import allure
import pytest

from courier_methods import CourierMethods
from data import CourierData


@allure.suite("Создание курьера")
class TestCreateCourier:

    @allure.title("Курьера можно успешно создать")
    def test_create_courier_with_valid_data_returns_201_and_true(
        self,
        courier_data
    ):
        response = CourierMethods.create_courier(courier_data)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title("Нельзя создать двух курьеров с одинаковым логином")
    def test_create_two_identical_couriers_returns_409(
        self,
        courier_data
    ):
        CourierMethods.create_courier(courier_data)
        second_response = CourierMethods.create_courier(courier_data)

        assert second_response.status_code == 409
        assert second_response.json()["message"] == (
            CourierData.EXISTING_LOGIN_MESSAGE
        )

    @allure.title("Без обязательного поля курьер не создаётся")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_without_required_field_returns_400(
        self,
        courier_data,
        missing_field
    ):
        courier_data.pop(missing_field)

        response = CourierMethods.create_courier(courier_data)

        assert response.status_code == 400
        assert response.json()["message"] == (
            CourierData.NOT_ENOUGH_DATA_MESSAGE
        )