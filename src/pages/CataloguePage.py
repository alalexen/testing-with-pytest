from src.pages.base_page import BasePage


class CataloguePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    BREADCRUMB = ("//ul[@class='breadcrumb']", "Catalogue breadcrumb", "xpath")

    def verify_catalogue_breadcrumb(self):
        breadcrumb_text = self.wait_until_element_visibility(self.BREADCRUMB).text
        assert breadcrumb_text == "Home Catalogue"