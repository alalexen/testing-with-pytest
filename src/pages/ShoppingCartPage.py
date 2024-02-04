from src.pages.page import Page
from selene import be
from selenium.webdriver.common.by import By


class ShoppingCartPage(Page):

    # CSS locators
    SHOPPING_CART_TITLE_CSS = "#basket > div.box > form > h1"

    # XPath locators
    CART_ITEM_XPATH = "//tr[@class='item']"
    TABLE_COLUMNS_XPATH = "//div[@class='table-responsive']//thead"
    QUANTITY_XPATH = "//input[@type='number']"

    def __init__(self, browser):
        super().__init__(browser)

    def verify_shopping_cart_is_opened(self):
        self.browser.element(self.SHOPPING_CART_TITLE_CSS).should(be.visible)

    def verify_shopping_cart_columns_name(self):
        column_names = self.browser.driver.find_element(By.XPATH, self.TABLE_COLUMNS_XPATH).text
        expected_columns_name = "Product Quantity Unit price Discount Total"
        assert column_names == expected_columns_name, \
            f"Expected columns name:\n {expected_columns_name} are not equal to actual ones:\n {column_names}"

    def verify_cart_items(self,
                          product: str = "Holy",
                          quantity: int = 1,
                          unit_price: float = 99.99,
                          discount: float = 0.00):

        actual_quantity = self.browser.driver.find_element(By.XPATH, self.QUANTITY_XPATH).get_attribute('value')

        items = self.browser.driver.find_element(
            By.XPATH, self.CART_ITEM_XPATH).text.replace('\n', " ").split(" ")

        assert actual_quantity == str(quantity),\
            f"Expected item's quantity {quantity} is not equal to actual one {actual_quantity}"

        assert items[0] == product,\
            f"Expected item's name {product} is not equal to actual one {items[0]}"
        assert items[1] == "$"+str(unit_price), \
            f"Expected item's quantity {quantity} is not equal to actual one {items[1]}"
        expected_discount = "$%.2f" % discount
        assert items[2] == expected_discount,\
            f"Expected item's discount {expected_discount} is not equal to actual one {items[2]}"
        expected_total = "$"+str(quantity*unit_price - discount)
        assert items[3] == expected_total,  \
            f"Expected item's total {expected_total} is not equal to actual one {items[3]}"
