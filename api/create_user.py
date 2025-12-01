import requests

from base_url import BASE_URL


class CreateUser:
    def __init__(self):
        self.base_url = BASE_URL

    def create_user(self, payload):
        return requests.post(f"{self.base_url}/api/auth/register", json=payload)
