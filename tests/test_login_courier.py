import requests
import allure
from endpoints import Endpoints
from data import Messages


class TestLoginCourier:

    @allure.title("Успешный логин курьера")
    def test_login_success(self, courier):
        credentials = {"login": courier["login"], "password": courier["password"]}
        with allure.step("Отправка запроса на логин"):
            response = requests.post(Endpoints.login_courier(), json=credentials)
        with allure.step("Проверка ответа"):
            assert response.status_code == 200
            assert isinstance(response.json()["id"], int)

    @allure.title("Ошибка 400 при логине без поля login")
    def test_login_missing_login(self, courier):
        credentials = {"password": courier["password"]}
        with allure.step("Отправка запроса без логина"):
            response = requests.post(Endpoints.login_courier(), json=credentials)
        with allure.step("Проверка ответа"):
            assert response.status_code == 400
            assert response.json()["message"] == Messages.NOT_ENOUGH_DATA_LOGIN

    @allure.title("Ошибка 400 при логине без поля password")
    def test_login_missing_password(self, courier):
        credentials = {"login": courier["login"]}
        with allure.step("Отправка запроса без пароля"):
            response = requests.post(Endpoints.login_courier(), json=credentials)
        with allure.step("Проверка ответа"):
            assert response.status_code == 400
            assert response.json()["message"] == Messages.NOT_ENOUGH_DATA_LOGIN

    @allure.title("Ошибка при логине с неверным паролем")
    def test_login_wrong_password(self, courier):
        credentials = {"login": courier["login"], "password": "wrongpass"}
        with allure.step("Отправка запроса с неверным паролем"):
            response = requests.post(Endpoints.login_courier(), json=credentials)
        with allure.step("Проверка ответа"):
            assert response.status_code == 404
            assert response.json()["message"] == Messages.USER_NOT_FOUND

    @allure.title("Ошибка при логине несуществующего пользователя")
    def test_login_nonexistent_user(self):
        credentials = {"login": "nonexistent_login_123", "password": "wrongpass"}
        with allure.step("Отправка запроса с несуществующим пользователем"):
            response = requests.post(Endpoints.login_courier(), json=credentials)
        with allure.step("Проверка ответа"):
            assert response.status_code == 404
            assert response.json()["message"] == Messages.USER_NOT_FOUND

