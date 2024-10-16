import pytest
import allure
import requests

@allure.title("Sample Testcase")
def test_sample():
    assert True == True
    print("Working fine")