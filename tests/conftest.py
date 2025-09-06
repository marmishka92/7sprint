import pytest
import requests
from endpoints import Endpoints
from helpers import register_new_courier_and_return_login_password, delete_courier
from data import TestData


@pytest.fixture
def courier_credentials():
    """Фикстура для создания курьера и получения его учетных данных"""
    login, password = register_new_courier_and_return_login_password()
    return {"login": login, "password": password}


@pytest.fixture
def courier():
    """Фикстура для создания курьера, его авторизации и последующей очистки"""
    courier_data = register_new_courier_and_return_login_password()
    login_data = TestData.create_login_data(courier_data[0], courier_data[1])

    response = requests.post(Endpoints.login_courier(), json=login_data)
    assert response.status_code == 200
    courier_id = response.json()["id"]

    yield {"id": courier_id, "login": courier_data[0], "password": courier_data[1]}

    delete_courier(courier_id)
