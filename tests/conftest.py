import sys
import os
import pytest
import requests
from urls import BASE_URL
from endpoints import Endpoints
from helpers import register_new_courier_and_return_login_password, delete_courier
from data import TestData

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


@pytest.fixture
def courier_credentials():
    """
    Фикстура для создания курьера и получения его учетных данных
    """
    login, password = register_new_courier_and_return_login_password()
    return {"login": login, "password": password}


@pytest.fixture
def courier():
    """
    Фикстура для создания курьера, его авторизации и последующей очистки
    """
    courier_data = register_new_courier_and_return_login_password()
    login_data = TestData.create_login_data(courier_data[0], courier_data[1])
    response = requests.post(BASE_URL + Endpoints.LOGIN_COURIER_EP, json=login_data)
    assert response.status_code == 200
    courier_id = response.json()["id"]

    yield {
        "id": courier_id,
        "login": courier_data[0],
        "password": courier_data[1]
    }

    delete_courier(courier_id)


def test_order_creation_with_payload(courier):
    """
    Тест для создания заказа с обычными данными
    """
    # Создаем заказ непосредственно в тесте
    order_payload = TestData.ORDER_DATA
    response = requests.post(BASE_URL + Endpoints.CREATE_ORDER_EP, json=order_payload)

    assert response.status_code == 201
    assert "id" in response.json()


def test_order_creation_with_alternative_data(courier):
    """
    Тест для создания заказа с альтернативными данными
    """
    # Создаем заказ с альтернативными данными непосредственно в тесте
    order_data = TestData.ALTERNATIVE_ORDER_DATA
    response = requests.post(BASE_URL + Endpoints.CREATE_ORDER_EP, json=order_data)

    assert response.status_code == 201
    assert "id" in response.json()
