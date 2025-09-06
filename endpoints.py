from urls import BASE_URL

class Endpoints:
    PREFIX = "/api/v1"

    @classmethod
    def create_courier(cls):
        return f"{BASE_URL}{cls.PREFIX}/courier"

    @classmethod
    def login_courier(cls):
        return f"{BASE_URL}{cls.PREFIX}/courier/login"

    @classmethod
    def delete_courier(cls, courier_id: int):
        return f"{BASE_URL}{cls.PREFIX}/courier/{courier_id}"

    @classmethod
    def create_order(cls):
        return f"{BASE_URL}{cls.PREFIX}/orders"

    @classmethod
    def get_order_list(cls):
        return f"{BASE_URL}{cls.PREFIX}/orders"
