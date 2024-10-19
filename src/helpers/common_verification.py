# Common verifcations
# HTTP Status Code
# Header
# Data verification
# JSON Schema

def verify_http_status_code(response_data, expected_data):
    assert response_data.status_code == expected_data, "Failed Status Code Match"

def verify_response_key(key, expected_data):
    assert key == expected_data

def verify_json_key_for_not_null(key): #key means json payload
    assert key != 0, "Failed - Key is non Empty" + key
    #assert key > 0, "Failed - Key is greater than zero"

def verify_json_key_for_not_null_token(key):
    assert key != 0, "Failed - Key is non empty" + key

def verify_response_delete(response):
    assert "created" in response

