

class AssertableResponse:
    def __init__(self, response):
        self._response = response

    def status_code(self, code):
        return self._response.status_code == code

    def field(self, name):
        return self._response.json()[name]
