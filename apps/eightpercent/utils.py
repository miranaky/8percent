from datetime import datetime


def validate_date_type(date: str, format) -> bool:
    if date is None:
        return False
    try:
        return bool(datetime.strptime(date, format))
    except ValueError:
        return False
