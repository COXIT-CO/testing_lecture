import time
from datetime import datetime


def get_time_of_day():
    """return string Night/Morning/Afternoon/Evening depending on the hours range"""
    now_time = datetime.now()
    if 0 <= now_time.hour <6:
        return "Night"
    if 6 <= now_time.hour < 12:
        return "Morning"
    if 12 <= now_time.hour <18:
        return "Afternoon"
    return "Evening"


def load_data():
    time.sleep(4)
    # loading data...
    return {"key1": "val1", "key2": "val2"}


def process_data():
    data = load_data()
    # process the data in certain ways ...
    processed_data = data["key1"]
    return processed_data