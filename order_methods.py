import allure
import requests

from urls import Urls


class OrderMethods:

    @staticmethod
    @allure.step("Создать заказ")
    def create_order(payload):
        return requests.post(
            Urls.ORDERS,
            json=payload
        )

    @staticmethod
    @allure.step("Получить список заказов")
    def get_orders():
        return requests.get(
            Urls.ORDERS
        )

    @staticmethod
    @allure.step("Отменить заказ")
    def cancel_order(track):
        return requests.put(
            f"{Urls.ORDERS}/cancel",
            params={"track": track}
        )