

def test_positive_login_with_valid_credentials(app):
    app.login_page().open()
    app.login_page().login("Margaret Camacho", "22986")