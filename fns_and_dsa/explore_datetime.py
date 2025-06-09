from datetime import datetime
from datetime import timedelta


def display_current_datetime():
    current_date = datetime.now()
    return current_date


def calculate_future_date():
    days = int(input('Enter the number of days to add to the current date:'))
    future_date  = display_current_datetime() + timedelta(days=days)
    return future_date.strftime('%Y-%m-%d')


def display_date():
    print(datetime.strftime(display_current_datetime(), '%Y-%m-%d %H:%M:%S'))
    print(f'Future date: {calculate_future_date()}')


if __name__ == "__main__":
    display_date()
