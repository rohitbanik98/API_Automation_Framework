Python API Automation Framework


Tech Stack
- Python 3.12
- Requests - HTTP Requests
- PyTest - Testing Framework
- Reporting - Allure report, Pytest HTML
- Test Data - CSV, Excel, Json, Faker
- Advance API Testcase - Jsonschema
- Parallel Execution - x distribute(xdist)

How to install packages

```pip install requests pytest pytest-html faker allure-pytest jsonschema python-dotenv```

How to runyour Testcase Parallel
```pip install pytest-xdist```

How to run a basic test with allure report
```pytest tests/tests/crud/test_create_booking.py --alluredir-allure_result -s```