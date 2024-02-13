import os


def test_negative_login_with_invalid_credentials(login_page, faker):
    login_page.open()
    login_page.login(faker.name(), faker.unique.first_name())
    login_page.verify_invalid_credentials_alert()


def test_negative_login_with_invalid_username(login_page, faker):
    login_page.open()
    login_page.login(faker.name(), os.environ['password'])
    login_page.verify_invalid_credentials_alert()


def test_negative_login_with_invalid_password(login_page, faker):
    login_page.open()
    login_page.login(os.environ["username"], faker.unique.first_name())
    login_page.verify_invalid_credentials_alert()


def test_negative_login_without_username(login_page):
    login_page.open()
    login_page.login("", os.environ["password"])
    login_page.verify_invalid_credentials_alert()


def test_negative_login_without_password(login_page):
    login_page.open()
    login_page.login(os.environ["username"], "")
    login_page.verify_invalid_credentials_alert()


def test_positive_login_with_valid_credentials(login_page):
    login_page.open()
    login_page.login(os.environ["username"], os.environ["password"])
    login_page.verify_successful_login()

