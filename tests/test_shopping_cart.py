import pytest


@pytest.fixture(scope='module', autouse=True)
def setup_module(login_page, config):
    login_page.login_as_admin(config)
    yield


def test_add_to_shopping_cart(login_page, home_page, shopping_cart_page):
    home_page.select_holy_socks()
    home_page.add_to_card()
    shopping_cart_page.navigate_to_shopping_cart()
    shopping_cart_page.verify_shopping_cart_columns_name()
    shopping_cart_page.verify_cart_items()


def test_navigate_back_to_catalogue(login_page, shopping_cart_page, catalogue_page):
    login_page.open()
    shopping_cart_page.navigate_to_shopping_cart()
    shopping_cart_page.click_continue_shopping_button()
    catalogue_page.verify_catalogue_breadcrumb()