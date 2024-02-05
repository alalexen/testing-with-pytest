from time import sleep

from src.pages.base_page import BasePage


class HomePage(BasePage):

    # CSS locators
    ADD_TO_CART_BUTTON = ("#buttonCart", "Add to cart button", "css")

    # XPath locators
    HOLY_SOCKS = ("//a[contains(text(), 'Holy')]", "Hoollly socks!", "xpath")

    def __init__(self, browser):
        super().__init__(browser)

    def select_holy_socks(self):
        self.click_web_element(self.HOLY_SOCKS)
        self.wait_until_element_visibility(self.ADD_TO_CART_BUTTON)

    def add_to_card(self):
        self.click_web_element(self.ADD_TO_CART_BUTTON)
        sleep(1)
