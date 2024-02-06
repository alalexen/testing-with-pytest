import configparser
import os.path
import sys
from faker import Faker

import pytest
from selene import Browser, Config
from selenium import webdriver

import allure

from src.pages.CataloguePage import CataloguePage
from src.pages.LoginPage import LoginPage
from src.pages.HomePage import HomePage
from src.pages.ProductDetailsPage import ProductDetailsPage
from src.pages.ShoppingCartPage import ShoppingCartPage


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
def config(request):
    config = get_config(request)
    return config


@pytest.fixture(scope="session")
def browser(config):
    browser = Browser(
        Config(
            driver=webdriver.Chrome(),
            base_url=config["base_url"],
            timeout=4

        )
    )
    yield browser
    browser.close()

# ------------------ Pages ---------------------


@allure.step
@pytest.fixture(scope="session")
def login_page(browser):
    return LoginPage(browser)


@allure.step
@pytest.fixture(scope="session")
def home_page(browser):
    return HomePage(browser)


@allure.step
@pytest.fixture(scope="session")
def product_details_page(browser):
    return ProductDetailsPage(browser)


@allure.step
@pytest.fixture(scope="session")
def shopping_cart_page(browser):
    return ShoppingCartPage(browser)


@allure.step
@pytest.fixture(scope="session")
def catalogue_page(browser):
    return CataloguePage(browser)

