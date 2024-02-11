from time import sleep
from src.pages.base_page import BasePage
from selene.support.conditions import be


class HomePage(BasePage):

    ADD_TO_CART_BUTTON = "#buttonCart"

    HOLY_SOCKS = "//a[contains(text(), 'Holy')]"

    def __init__(self, browser):
        super().__init__(browser)

    def select_holy_socks(self):
        self.click_web_element(self.HOLY_SOCKS)
        self.browser.element(self.ADD_TO_CART_BUTTON).should(be.visible)

    def add_to_card(self):
        self.click_web_element(self.ADD_TO_CART_BUTTON)
        sleep(1)
