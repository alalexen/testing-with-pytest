from src.pages.LoginPage import LoginPage
from src.pages.HomePage import HomePage
from src.pages.ProductDetailsPage import ProductDetailsPage
from src.pages.ShoppingCartPage import ShoppingCartPage


class Application:

    def __init__(self, browser, config):
        self.browser = browser
        self.config = config

    def login_page(self):
        return LoginPage(self.browser)

    def home_page(self):
        return HomePage(self.browser)

    def product_details_page(self):
        return ProductDetailsPage(self.browser)

    def shopping_cart_page(self):
        return ShoppingCartPage(self.browser)
