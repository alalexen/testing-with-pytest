import configparser
import os.path
import sys
from faker import Faker

import pytest
from selene import Browser, Config
from selenium import webdriver

from src.pages.app import Application


@pytest.fixture
def faker():
    return Faker()


def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="local", help="env variable name"
    )


def read_ini():
    config_file_name = os.environ.get("config-file", "project-config.ini")
    root_path = os.path.join(sys.path[0], config_file_name)
    parser = configparser.ConfigParser()
    parser.read(root_path)
    return parser


# pytest tests/test_login.py --env=local

def get_config(request):
    env_name = request.config.getoption('--env')
    try:
        return read_ini()[env_name]
    except KeyError:
        raise Exception(f"Wrong configuration [{env_name}]")


@pytest.fixture(scope="session")
def browser(request):
    config = get_config(request)
    browser = Browser(
        Config(
            driver=webdriver.Chrome(),
            base_url=config["base_url"],
            timeout=4

        )
    )
    yield browser
    browser.close()


@pytest.fixture(scope="session")
def app(browser, request):
    config = get_config(request)
    return Application(browser, config)

