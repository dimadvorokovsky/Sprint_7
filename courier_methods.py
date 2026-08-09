import allure
import requests

from urls import Urls


class CourierMethods:

    @staticmethod
    @allure.step("Создать курьера")
    def create_courier(payload):
        return requests.post(
            Urls.CREATE_COURIER,
            data=payload
        )

    @staticmethod
    @allure.step("Авторизовать курьера")
    def login_courier(payload):
        return requests.post(
            Urls.LOGIN_COURIER,
            data=payload
        )

    @staticmethod
    @allure.step("Удалить курьера")
    def delete_courier(courier_id):
        return requests.delete(
            f"{Urls.CREATE_COURIER}/{courier_id}"
        )