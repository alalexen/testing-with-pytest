from selene import have
from src.pages.page import Page
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(Page):
    def __init__(self, browser):
        super().__init__(browser)
        self.wait = 5

    def wait_until_element_visibility(self, locator):
        try:
            wait = WebDriverWait(self.browser.driver, self.wait)
            return wait.until(EC.visibility_of(locator))
        except TimeoutException:
            print(f"Element {locator} is not displayed after {self.wait} sec")

    def click_web_element(self, element_locator):
        self.browser.element(element_locator).click()

    def set_element_text(self, element_locator, value):
        self.browser.element(element_locator).type(value)

    def verify_element_text(self, element_locator, expected_text):
        self.browser.element(element_locator).should(have.text(expected_text))

    def verify_element_value(self, element_locator, expected_value):
        self.browser.element(element_locator).should(have.value(expected_value))

