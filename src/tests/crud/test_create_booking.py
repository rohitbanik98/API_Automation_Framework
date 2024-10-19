# API Testcase

# URL - api_constants.py
#headers - utils.py
#payloads - payload_manager.py
#HTTP POST - api_requests_wrapper.py
#verification - common_verification.py

import allure
import pytest
import requests

from src.constants.api_constants import APIConstants
from src.helpers.Api_requests_wrapper import post_request
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verification import *
from src.utils.utils import Utils
import logging

class TestCreateBooking():
    @allure.title("TC1 - Create booking")
    @pytest.mark.positive
    @allure.description("Verify that Create Booking Status and Booking ID shouldn't be null")
    def test_create_booking_positive(self):
        LOGGER = logging.getLogger()
        LOGGER.info("Starting of TC1")
        response = post_request(url=APIConstants().url_create_booking(),
                                auth=None,
                                headers=Utils().common_headers_json(),
                                payload=payload_create_booking(),
                                in_json=False)
        verify_http_status_code(response_data=response, expected_data=200)
        verify_json_key_for_not_null(response.json()["bookingid"])
        LOGGER.info(response.json()["bookingid"])
        LOGGER.info("End of the Testcase TC1 -positive")

    @allure.title("TC2 - Create booking")
    @pytest.mark.negative
    @allure.description("Verify that Create Booking Status should be 500")
    def test_create_booking_negative(self):
        print("Starting of TC2")
        response = post_request(url=APIConstants().url_create_booking(),
                                auth=None,
                                headers=Utils().common_headers_json(),
                                payload={},
                                in_json=False)
        verify_http_status_code(response_data=response, expected_data= 500)
