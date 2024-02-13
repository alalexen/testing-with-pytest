import abc
import jsonpath_rw
from hamcrest import assert_that


class Conditions:
    def __init__(self):
        pass

    @abc.abstractmethod
    def match(self, response):
        return


class StatusCodeCondition(Conditions):

    def __init__(self, code):
        super().__init__()
        self._status_code = code

    def __repr__(self):
        return f"status code is {self._status_code}"

    def match(self, response):
        assert response.status_code == self._status_code


status_code = StatusCodeCondition


class BodyFieldCondition(Conditions):
    def __init__(self, json_path, matcher):
        super().__init__()
        self._json_path = json_path
        self._matcher = matcher

    def __repr__(self):
        return f"body field {self._json_path} {self._matcher}"

    def match(self, response):
        json = response.json()
        value = jsonpath_rw.parse(self._json_path).find(json)
        assert_that(value, self._matcher)


body = BodyFieldCondition





