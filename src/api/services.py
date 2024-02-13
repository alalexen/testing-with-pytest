import os
import requests
import json
from src.api.response import AssertableResponse


class ApiServices:
    def __init__(self):
        self.header = {'content-type': 'application/json'}
        self._base_url = os.environ['BASE_URL']

    def _post(self, body):
        token = None
        return requests.post(f"{self._base_url}/register", data=json.dumps(body),
                             headers=self.header)

    # def auth(self):  # for apps with jwt token auth type
    #     return requests.post("your_auth_service").json()["token"]


class UserApiService(ApiServices):
    def __init__(self):
        super().__init__()

    def create_user(self, user):
        # token = self.auth()
        # return AssertableResponse(self._post(user, token))

        return AssertableResponse(self._post(user))
