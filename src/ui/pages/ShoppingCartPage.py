
from src.ui.pages.base_page import BasePage
from selene.support.conditions import be
from selene import by


class ShoppingCartPage(BasePage):

    SHOPPING_CART_TITLE = "#basket > div.box > form > h1"
    X_ITEMS_IN_CART_BUTTON = "#numItemsInCart"

    CART_ITEM = "//tr[@class='item']"
    TABLE_COLUMNS = "//div[@class='table-responsive']//thead"
    QUANTITY = "//input[@type='number']"
    CONTINUE_SHOPPING_BUTTON = "//div[@class='pull-left']//a[@class='btn btn-default']"

    def __init__(self, browser):
        super().__init__(browser)

    def navigate_to_shopping_cart(self):
        self.click_web_element(self.X_ITEMS_IN_CART_BUTTON)
        # self.wait_until_element_visibility(self.SHOPPING_CART_TITLE)
        self.browser.element(self.SHOPPING_CART_TITLE).should(be.visible)

    def verify_shopping_cart_columns_name(self):
        expected_columns_name = "Product Quantity Unit price Discount Total"
        self.verify_element_text(self.TABLE_COLUMNS, expected_columns_name)

    def verify_cart_items(self,
                          product: str = "Holy",
                          quantity: int = 1,
                          unit_price: float = 99.99,
                          discount: float = 0.00):

        self.verify_element_value(self.QUANTITY, str(quantity))

        items = self.wait_until_element_visibility(by.xpath(self.CART_ITEM)).text.replace('\n', " ").split(" ")
        #replace native selenium method by selene

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

    def click_continue_shopping_button(self):
        self.click_web_element(self.CONTINUE_SHOPPING_BUTTON)
