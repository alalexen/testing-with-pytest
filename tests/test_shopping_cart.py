
def test_add_to_shopping_cart(app):
    app.login_page().login_as_admin(app)
    app.home_page().select_holy_socks()
    app.home_page().add_to_card()
    app.shopping_cart_page().navigate_to_shopping_cart()
    app.shopping_cart_page().verify_shopping_cart_columns_name()
    app.shopping_cart_page().verify_cart_items()


def test_navigate_back_to_catalogue(app):
    app.login_page().login_as_admin(app)
    app.shopping_cart_page().navigate_to_shopping_cart()
    app.shopping_cart_page().click_continue_shopping_button()
    app.catalogue_page().verify_catalogue_breadcrumb()
