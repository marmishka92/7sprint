class TestData:
    valid_courier = {
        "login": "unique_login",
        "password": "valid_password",
        "firstName": "SomeName"
    }

    @staticmethod
    def create_login_data(login, password):
        return {
            "login": login,
            "password": password
        }



