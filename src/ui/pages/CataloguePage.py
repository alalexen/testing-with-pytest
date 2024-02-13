from src.ui.pages.base_page import BasePage


class CataloguePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    BREADCRUMB = "//ul[@class='breadcrumb']"

    def verify_catalogue_breadcrumb(self):
        self.verify_element_text(self.BREADCRUMB, "Home Catalogue")
