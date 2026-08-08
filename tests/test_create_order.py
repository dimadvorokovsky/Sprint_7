import copy

import allure
import pytest

from data import OrderData
from order_methods import OrderMethods


@allure.suite("Создание заказа")
class TestCreateOrder:

    @allure.title("Заказ можно создать с разными вариантами цвета")
    @pytest.mark.parametrize("color", OrderData.COLORS)
    def test_create_order_with_different_colors_returns_201_and_track(
        self,
        color
    ):
        order_data = copy.deepcopy(OrderData.BASE_ORDER)
        order_data["color"] = color

        response = OrderMethods.create_order(order_data)

        assert response.status_code == 201
        assert "track" in response.json()

        track = response.json()["track"]
        OrderMethods.cancel_order(track)