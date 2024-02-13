from src.api.services import UserApiService


def test_positive_register_user_with_valid_creds(faker):
    user = {"username": faker.name(), "password": "12345", "email": "demo@gmail.com"}
    resp = UserApiService().create_user(user)
    assert resp.status_code(200)
    assert len(resp.field('id')) > 0


def test_negative_register_user_with_same_creds_twice(faker):
    user_api = UserApiService()
    user = {"username": faker.name(), "password": "12345", "email": "demo@gmail.com"}
    resp1 = user_api.create_user(user)
    assert resp1.status_code(200)
    resp2 = user_api.create_user(user)
    assert resp2.status_code(500)