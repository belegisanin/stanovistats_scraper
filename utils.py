from datetime import datetime
import hashlib


def parse_date(date_str: str) -> datetime:
    # Example format: "31.12.2024."
    # Adjust the format string according to your actual date format
    format_str = "%d.%m.%Y."
    return datetime.strptime(date_str, format_str) if date_str else None


def static_hash(string: str) -> str:
    return hashlib.md5(string.encode()).hexdigest()
