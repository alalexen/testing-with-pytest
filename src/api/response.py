import logging


class AssertableResponse:
    def __init__(self, response):
        logging.info(f"\nRequest:"
                     f"\n   url = {response.request.url}"
                     f"\n   body = {response.request.body}")
        logging.info(f"\nResponse: "
                     f"\n   body = {response.text if response.text else None}"
                     f"\n   status = {response.status_code if response.status_code else None}")
        self._response = response

    def status_code(self, code):
        logging.info(f"status code should be {code}")
        return self._response.status_code == code

    def field(self, name):
        return self._response.json()[name]
