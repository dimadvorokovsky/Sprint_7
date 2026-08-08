import requests

from urls import Urls


class OrderMethods:
    @staticmethod
    def create_order(payload):
        return requests.post(
            Urls.ORDERS,
            json=payload
        )

    @staticmethod
    def get_orders():
        return requests.get(
            Urls.ORDERS
        )

    @staticmethod
    def cancel_order(track):
        return requests.put(
            f"{Urls.ORDERS}/cancel",
            params={"track": track}
        )