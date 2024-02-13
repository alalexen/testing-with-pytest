import logging
import allure


class AssertableResponse:
    def __init__(self, response):
        request_log = f"Request: url = {response.request.url}, body = {response.request.body}"
        resp_log = (f"Response: body = {response.text if response.text else None}, "
                    f"status = {response.status_code if response.status_code else None}")

        logging.info(request_log)
        logging.info(resp_log)

        self._response = response

    # @allure.step('status code should be {code}')
    # def status_code(self, code):
    #     logging.info(f"assert: status code should be {code}")
    #     return self._response.status_code == code
    #
    # @allure.step
    # def field(self, name):
    #     return self._response.json()[name]

    @allure.step('response should have {condition}')
    def should_have(self, condition):
        logging.info(f"About to check {condition}")
        condition.match(self._response)


