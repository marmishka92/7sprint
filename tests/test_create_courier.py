import pytest
import requests
import allure
from endpoints import Endpoints
from helpers import generate_unique_user
from data import Messages


class TestCreateCourier:

    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self):
        courier_data = generate_unique_user()
        with allure.step("Отправка запроса на создание курьера"):
            response = requests.post(Endpoints.create_courier(), json=courier_data)
        with allure.step("Проверка ответа"):
            assert response.status_code == 201
            assert response.json()["ok"] is True

    @allure.title("Ошибка при создании курьера с существующим логином")
    def test_create_duplicate_courier(self, courier):
        duplicate_data = {
            "login": courier["login"],
            "password": "different_password",
            "firstName": "different_name"
        }
        with allure.step("Отправка запроса на создание дубликата"):
            response = requests.post(Endpoints.create_courier(), json=duplicate_data)
        with allure.step("Проверка ответа"):
            assert response.status_code == 409
            assert response.json()["message"] == Messages.LOGIN_ALREADY_USED

    @allure.title("Ошибка при создании курьера без обязательного поля")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_missing_required_field(self, missing_field):
        courier_data = generate_unique_user()
        courier_data.pop(missing_field)
        with allure.step(f"Отправка запроса без поля {missing_field}"):
            response = requests.post(Endpoints.create_courier(), json=courier_data)
        with allure.step("Проверка ответа"):
            assert response.status_code == 400
            assert response.json()["message"] == Messages.NOT_ENOUGH_DATA_CREATE

    @allure.title("Ошибка при создании курьера с одинаковым логином и разным паролем")
    def test_create_courier_same_login_different_password(self, courier):
        duplicate_data = {
            "login": courier["login"],
            "password": "different_password",
            "firstName": "different_name"
        }
        with allure.step("Отправка запроса на создание курьера с одинаковым логином"):
            response = requests.post(Endpoints.create_courier(), json=duplicate_data)
        with allure.step("Проверка ответа"):
            assert response.status_code == 409
            assert response.json()["message"] == Messages.LOGIN_ALREADY_USED
