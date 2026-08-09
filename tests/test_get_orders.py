import allure

from order_methods import OrderMethods


@allure.suite("Получение списка заказов")
class TestGetOrders:

    @allure.title("В ответе возвращается список заказов")
    def test_get_orders_returns_200_and_orders_list(self):
        response = OrderMethods.get_orders()

        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)