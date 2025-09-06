import re

def validate_phone(phone: str) -> bool:
    pattern = r'^\+?[1-9]\d{1,14}$'
    return bool(re.match(pattern, phone))

def validate_area(area: str) -> bool:
    try:
        float(area)
        return True
    except ValueError:
        return False