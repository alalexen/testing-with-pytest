from src.pages.page import Page
from selene import have
from selene.api import by


class LoginPage(Page):

    # CSS locators
    LOGIN_BUTTON_HEADER_CSS = "#login"
    USERNAME_FIELD_CSS = "#username-modal"
    PASSWORD_FIELD_CSS = "#password-modal"
    LOGGED_IN_AS_CSS = "#howdy > a"

    # XPath locators
    CONFIRM_LOGIN_BUTTON_XPATH = "//button[@class='btn btn-primary']"

    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.open("")

    def login(self, username, password):
        self.browser.element(self.LOGIN_BUTTON_HEADER_CSS).click()
        self.browser.element(self.USERNAME_FIELD_CSS).set_value(username)
        self.browser.element(self.PASSWORD_FIELD_CSS).set_value(password)
        self.browser.element(by.xpath(self.CONFIRM_LOGIN_BUTTON_XPATH)).click()
        self.browser.element(self.LOGGED_IN_AS_CSS).should(have.exact_text("Logged in as"))

    def login_as_admin(self, app):
        self.open()
        self.login(
            app.config["username"],
            app.config["password"]
        )

