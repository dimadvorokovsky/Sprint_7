import allure
import pytest

from courier_methods import CourierMethods


@allure.suite("Логин курьера")
class TestLoginCourier:

    @allure.title("Курьер может успешно авторизоваться")
    def test_login_courier_with_valid_data_returns_200_and_id(self, courier):
        login_data = {
            "login": courier["login"],
            "password": courier["password"]
        }

        response = CourierMethods.login_courier(login_data)

        assert response.status_code == 200
        assert isinstance(response.json()["id"], int)

    @allure.title("Для авторизации нужно передать все обязательные поля")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_login_courier_without_required_field_returns_400(
        self,
        courier,
        missing_field
    ):
        login_data = {
            "login": courier["login"],
            "password": courier["password"]
        }
        login_data.pop(missing_field)

        response = CourierMethods.login_courier(login_data)

        assert response.status_code == 400
        assert response.json()["message"] == (
            "Недостаточно данных для входа"
        )

    @allure.title("При неправильном логине система возвращает ошибку")
    def test_login_courier_with_wrong_login_returns_404(self, courier):
        login_data = {
            "login": f"wrong_{courier['login']}",
            "password": courier["password"]
        }

        response = CourierMethods.login_courier(login_data)

        assert response.status_code == 404
        assert response.json()["message"] == (
            "Учетная запись не найдена"
        )

    @allure.title("При неправильном пароле система возвращает ошибку")
    def test_login_courier_with_wrong_password_returns_404(self, courier):
        login_data = {
            "login": courier["login"],
            "password": "wrong_password"
        }

        response = CourierMethods.login_courier(login_data)

        assert response.status_code == 404
        assert response.json()["message"] == (
            "Учетная запись не найдена"
        )

    @allure.title("Несуществующий курьер не может авторизоваться")
    def test_login_nonexistent_courier_returns_404(self):
        login_data = {
            "login": "nonexistent_courier_login",
            "password": "nonexistent_password"
        }

        response = CourierMethods.login_courier(login_data)

        assert response.status_code == 404
        assert response.json()["message"] == (
            "Учетная запись не найдена"
        )