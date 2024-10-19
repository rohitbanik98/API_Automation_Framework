from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import *
from src.helpers.Api_requests_wrapper import *
from src.helpers.common_verification import *
from src.utils.utils import Utils

import allure
import pytest

@pytest.fixture(scope="session")
def create_token():
    response = post_request(
        url=APIConstants().url_create_token(),
        headers=Utils().common_headers_json(),
        payload=payload_create_token(),
        auth=None,
        in_json=False,
    )
    verify_http_status_code(response,expected_data=200)
    verify_json_key_for_not_null(response.json()["token"])
    return response.json()["token"]


@pytest.fixture(scope="session")
def get_booking_id():
    response = post_request(
        url=APIConstants().url_create_booking(),
        auth= None,
        headers=Utils().common_headers_json(),
        payload=payload_create_booking(),
        in_json=False,
    )
    verify_http_status_code(response, expected_data=200)
    verify_json_key_for_not_null_token(response.json()["bookingid"])
    return response.json()["bookingid"]