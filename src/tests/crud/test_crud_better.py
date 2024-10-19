#Conftest

# Create Token
# Create Booking Id
# Update the Booking(Put) - BookingID,Token
# Delete the Booking

# Integration testing scenarios:

#Verify that created booking id when we update we are able to update it and delete it also

from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import *
from src.helpers.Api_requests_wrapper import *
from src.helpers.common_verification import *
from src.utils.utils import Utils

import allure
import pytest

class TestCRUDBooking():

    @allure.title("Test CRUD operations Update(PUT)")
    @allure.description("Verify that full update with the booking ID and Token is working")
    def test_update_booking_id_token(self,create_token, get_booking_id):
        put_URL = APIConstants().url_patch_put_delete(booking_id=get_booking_id)
        response = put_request(
            url=put_URL,
            headers=Utils().common_headers_put_delete_patch_cookie(token=create_token),
            payload= payload_create_booking(),
            auth=None,
            in_json=False,
        )
        verify_http_status_code(response,expected_data=200)
        print(get_booking_id)
        print(create_token)
        print(response.json())
        verify_response_key(response.json()["firstname"], expected_data="Rohit")
        verify_response_key(response.json()["lastname"], expected_data="Banik")


    def test_delete_booking_id(self,get_booking_id,create_token):
        delete_URL = APIConstants().url_patch_put_delete(booking_id=get_request)
        print(get_booking_id)
        print(create_token)
        response = delete_requests(
            url=delete_URL,
            headers=Utils().common_headers_put_delete_patch_cookie(token=create_token),
            auth=None,
            in_json=False,
        )
        verify_http_status_code(response,expected_data=405)#in postman the code is 201
