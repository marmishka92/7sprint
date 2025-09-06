import requests
import random
import string
from endpoints import Endpoints


def register_new_courier_and_return_login_password():
    def gen(length=10):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

    login = gen()
    password = gen()
    first_name = gen()

    payload = {"login": login, "password": password, "firstName": first_name}
    response = requests.post(Endpoints.create_courier(), json=payload)

    if response.status_code == 201:
        return [login, password, first_name]
    return []


def generate_unique_user():
    def gen(length=10):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
    return {"login": gen(), "password": gen(), "firstName": gen()}


def delete_courier(courier_id):
    return requests.delete(Endpoints.delete_courier(courier_id))

