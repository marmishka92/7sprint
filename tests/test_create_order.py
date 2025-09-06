import pytest
import requests
import allure
from endpoints import Endpoints
from data import TestData


class TestCreateOrder:

    @allure.title("Создание заказа с обычными данными")
    def test_order_creation_with_payload(self, courier):
        with allure.step("Отправка запроса на создание заказа с обычными данными"):
            response = requests.post(Endpoints.create_order(), json=TestData.ORDER_DATA)
        with allure.step("Проверка ответа"):
            assert response.status_code == 201
            assert "track" in response.json()

    @allure.title("Создание заказа с альтернативными данными")
    def test_order_creation_with_alternative_data(self, courier):
        with allure.step("Отправка запроса на создание заказа с альтернативными данными"):
            response = requests.post(Endpoints.create_order(), json=TestData.ALTERNATIVE_ORDER_DATA)
        with allure.step("Проверка ответа"):
            assert response.status_code == 201
            assert "track" in response.json()

    @allure.title("Создание заказа с разными вариантами цветов")
    @pytest.mark.parametrize("colors", [
        ["BLACK"], ["GREY"], ["BLACK", "GREY"], []
    ])
    def test_create_order_colors(self, colors):
        order_data = TestData.ORDER_DATA.copy()
        order_data["color"] = colors
        with allure.step(f"Отправка запроса на создание заказа с цветами {colors}"):
            response = requests.post(Endpoints.create_order(), json=order_data)
        with allure.step("Проверка ответа"):
            assert response.status_code == 201
            assert "track" in response.json()
            assert isinstance(response.json()["track"], int)
