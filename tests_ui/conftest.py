import os

import allure
import pytest
from selenium import webdriver
from selene import Browser, Config
from src.ui.pages.HomePage import HomePage
from src.ui.pages.LoginPage import LoginPage
from src.ui.pages.CataloguePage import CataloguePage
from src.ui.pages.ShoppingCartPage import ShoppingCartPage
from src.ui.pages.ProductDetailsPage import ProductDetailsPage
from common.conftest import pytest_addoption, faker


def ui_faker():
    return faker


def ui_pytest_addoption(parser):
    pytest_addoption(parser)

# read project-config.ini file
# def ui_config(request):
#     return config(request)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(autouse=True)
def log_on_failure(request, browser):
    yield
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        allure.attach(browser.driver.get_screenshot_as_png(),
                      name=request.node.name,
                      attachment_type=allure.attachment_type.PNG)


@pytest.fixture(scope="session")
def browser():
    browser = Browser(
        Config(
            driver=webdriver.Chrome(),
            base_url=os.environ['BASE_URL'],
            timeout=4

        )
    )
    yield browser
    browser.close()


# Pages

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

