import requests

from base_url import BASE_URL


class LoginUser:
    def __init__(self):
        self.base_url = BASE_URL
        self.token = ''

    def login_user(self, payload):
        response = requests.post(f"{self.base_url}/api/auth/login", json=payload)
        self.token = response.json()['accessToken']
        return response
