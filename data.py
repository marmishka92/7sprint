class Messages:
    LOGIN_ALREADY_USED = "Этот логин уже используется. Попробуйте другой."
    NOT_ENOUGH_DATA_CREATE = "Недостаточно данных для создания учетной записи"
    NOT_ENOUGH_DATA_LOGIN = "Недостаточно данных для входа"
    USER_NOT_FOUND = "Учетная запись не найдена"


class TestData:
    valid_courier = {
        "login": "unique_login",
        "password": "valid_password",
        "firstName": "SomeName"
    }

    @staticmethod
    def create_login_data(login, password):
        return {"login": login, "password": password}

    ORDER_DATA = {
        "firstName": "Иван",
        "lastName": "Иванов",
        "address": "Москва, ул. Пушкина, д. 10",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2024-03-20",
        "comment": "Позвонить за час",
        "color": ["BLACK"]
    }

    ALTERNATIVE_ORDER_DATA = {
        "firstName": "Петр",
        "lastName": "Петров",
        "address": "СПб, Невский пр., д. 1",
        "metroStation": 10,
        "phone": "+7 911 123 45 67",
        "rentTime": 3,
        "deliveryDate": "2024-03-25",
        "comment": "Доставка вечером",
        "color": ["GREY"]
    }