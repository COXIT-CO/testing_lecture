import pytest
from datetime import datetime
from src.app import get_time_of_day, process_data


def test_get_time_of_day(mocker):
    mock_now = mocker.patch("src.app.datetime")
    mock_now.now.return_value = datetime(2016, 5, 20, 14, 10, 0)

    assert get_time_of_day() == "Afternoon"


@pytest.mark.parametrize(
    "datetime_obj, expect",
    [
        (datetime(2016, 5, 20, 0, 0, 0), "Night"),
        (datetime(2016, 5, 20, 1, 10, 0), "Night"),
        (datetime(2016, 5, 20, 6, 10, 0), "Morning"),
        (datetime(2016, 5, 20, 12, 0, 0), "Afternoon"),
        (datetime(2016, 5, 20, 14, 10, 0), "Afternoon"),
        (datetime(2016, 5, 20, 18, 0, 0), "Evening"),
        (datetime(2016, 5, 20, 19, 10, 0), "Evening"),
    ],
)
def test_get_time_of_day(datetime_obj, expect, mocker):
    mock_now = mocker.patch("src.app.datetime")
    mock_now.now.return_value = datetime_obj

    assert get_time_of_day() == expect


def test_process_data(mocker):
    mocker.patch("src.app.load_data", return_value={"key1": "valy", "key2": "val2"})
    assert process_data() == "valy"
