import allure
from src.pages.base_page import BasePage


class LoginPage(BasePage):

    # CSS locators
    LOGIN_BUTTON_HEADER = ("#login", "Login button from header", "css")
    USERNAME_FIELD = ("#username-modal", "Username field", "css")
    PASSWORD_FIELD = ("#password-modal", "Password field", "css")
    LOGGED_IN_AS = ("#howdy > a", "Logged as href", "css")

    # XPath locators
    CONFIRM_LOGIN_BUTTON = ("//button[@class='btn btn-primary']", "Confirm login button", "xpath")
    INVALID_CREDS_ALERT = ("//div[@class='alert alert-danger']", "Invalid credentials alert", "xpath")

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("open browser and navigate to url")
    def open(self):
        self.browser.open("")

    @allure.step
    def login(self, username, password):
        self.click_web_element(self.LOGIN_BUTTON_HEADER)
        self.set_element_text(self.USERNAME_FIELD, username)
        self.set_element_text(self.PASSWORD_FIELD, password)
        self.click_web_element(self.CONFIRM_LOGIN_BUTTON)

    def verify_successful_login(self):
        self.verify_element_text(self.LOGGED_IN_AS, "Logged in as")

    def login_as_admin(self, config):
        self.open()
        self.login(
            config["username"],
            config["password"]
        )

    def verify_invalid_credentials_alert(self):
        self.verify_element_text(self.INVALID_CREDS_ALERT, "Invalid login credentials.")