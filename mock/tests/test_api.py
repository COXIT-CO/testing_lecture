import pytest
from src.some_api import Employee

emp_1 = Employee("Corey", "Schafer", 50000)


def test_mock_api_call(mocker):
    mock_requests = mocker.patch("requests.get")
    mock_requests.return_value.ok = True
    mock_requests.return_value.text = "Success"

    schedule = emp_1.monthly_schedule("May")
    assert schedule == "Success"
