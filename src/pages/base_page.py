from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from src.pages.page import Page

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(Page):
    def __init__(self, browser):
        super().__init__(browser)
        self.wait = 5

    @staticmethod
    def get_locator(locator_type):
        return_by = None
        if locator_type == "xpath":
            return_by = By.XPATH
        elif locator_type == "css":
            return_by = By.CSS_SELECTOR
        elif locator_type == "id":
            return_by = By.ID
        return return_by

    def wait_until_element_visibility(self, locator):
        by_selector = self.get_locator(locator[2])
        try:
            wait = WebDriverWait(self.browser.driver, self.wait)
            return wait.until(EC.visibility_of_element_located((by_selector, locator[0])))
        except TimeoutException:
            print(f"Element {locator[0]} ({locator[1]}) is not displayed after {self.wait} sec")

    def click_web_element(self, element_locator):
        element = self.wait_until_element_visibility(element_locator)
        element.click()

    def set_element_text(self, element_locator, value):
        element = self.wait_until_element_visibility(element_locator)
        element.send_keys(value)

    def verify_element_text(self, element_locator, text):
        element = self.wait_until_element_visibility(element_locator)
        assert element.text == text, f"Expected text {text} is not equal to actual {element.text}"
