from common.conftest import pytest_addoption, faker


def api_pytest_addoption(parser):
    pytest_addoption(parser)


def api_faker():
    return faker
