import requests
import allure
from endpoints import Endpoints


class TestOrderList:

    @allure.title("Получение списка заказов")
    def test_get_order_list_returns_orders_list(self):
        with allure.step("Отправка запроса на получение списка заказов"):
            response = requests.get(Endpoints.get_order_list())
        with allure.step("Проверка ответа"):
            assert response.status_code == 200
            assert isinstance(response.json()["orders"], list)
