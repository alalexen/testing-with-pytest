

def test_negative_login_with_invalid_credentials(app, faker):
    app.login_page().open()
    app.login_page().login(faker.name(), faker.unique.first_name())
    app.login_page().verify_invalid_credentials_alert()


def test_negative_login_with_invalid_username(app, faker):
    app.login_page().open()
    app.login_page().login(faker.name(), app.config["password"])
    app.login_page().verify_invalid_credentials_alert()


def test_negative_login_with_invalid_password(app, faker):
    app.login_page().open()
    app.login_page().login(app.config["username"], faker.unique.first_name())
    app.login_page().verify_invalid_credentials_alert()


def test_negative_login_without_username(app):
    app.login_page().open()
    app.login_page().login("", app.config["password"])
    app.login_page().verify_invalid_credentials_alert()


def test_negative_login_without_password(app):
    app.login_page().open()
    app.login_page().login(app.config["username"], "")
    app.login_page().verify_invalid_credentials_alert()


def test_positive_login_with_valid_credentials(app):
    app.login_page().open()
    app.login_page().login(app.config["username"], app.config["password"])
    app.login_page().verify_successful_login()

