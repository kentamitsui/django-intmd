from datetime import date, datetime
from typing import Any


def str_to_date(date_of_birth: str) -> datetime.date:
    date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
    return date_of_birth


def get_age_from_date_of_birth(date_of_birth: Any) -> int:
    if isinstance(date_of_birth, str):
        date_of_birth = str_to_date(date_of_birth)
    if not isinstance(date_of_birth, date):
        raise ValueError("Invalid date of type")

    today = date.today()
    age = today.year - date_of_birth.year
    if (today.month, today.day) < (date_of_birth.month, date_of_birth.day):
        age -= 1
    return age
