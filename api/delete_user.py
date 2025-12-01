import requests

from base_url import BASE_URL


class DeleteUser:
    def __init__(self):
        self.base_url = BASE_URL

    def delete_user(self, token):
        headers = {
            'Authorization': token
        }
        return requests.delete(f"{self.base_url}/api/auth/user", headers=headers)
