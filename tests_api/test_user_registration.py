from src.api.services import UserApiService
from src.api.conditions import status_code, body
from src.api.payload_utils import generate_user_data
from hamcrest import has_length, greater_than


def test_positive_register_user_with_valid_creds(faker):
    resp = UserApiService().create_user(generate_user_data(faker))
    resp.should_have(status_code(200))
    resp.should_have(body('$.id', has_length(greater_than(0))))


def test_negative_register_user_with_same_creds_twice(faker):
    user = generate_user_data(faker)
    resp1 = UserApiService().create_user(user)
    resp1.should_have(status_code(200))
    resp2 = UserApiService().create_user(user)
    resp2.should_have(status_code(500))
