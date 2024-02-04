from selene import be, have

from src.pages.page import Page
from selene.api import by


class HomePage(Page):

    # CSS locators
    ADD_TO_CART_BUTTON_CSS = "#buttonCart"
    X_ITEMS_IN_CART_BUTTON_CSS = "#numItemsInCart"

    # XPath locators
    HOLY_SOCKS_XPATH = "//a[contains(text(), 'Holy')]"

    def __init__(self, browser):
        super().__init__(browser)

    def select_holy_socks(self):
        self.browser.element(by.xpath(self.HOLY_SOCKS_XPATH)).click()
        self.browser.element(self.ADD_TO_CART_BUTTON_CSS).should(be.visible)

    def add_to_card(self):
        self.browser.element(self.ADD_TO_CART_BUTTON_CSS).click()

    def verify_items_in_cart_button(self, items_amount: int):
        self.browser.element(self.X_ITEMS_IN_CART_BUTTON_CSS).should(
            have.exact_text(
                "{} item(s) in cart".format(str(items_amount))
            )
        )

    def navigate_to_shopping_cart(self):
        self.browser.element(self.X_ITEMS_IN_CART_BUTTON_CSS).click()
