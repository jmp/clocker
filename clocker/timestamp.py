from datetime import datetime, timezone
from typing import Optional


class Timestamp:
    _value: datetime

    def __init__(self, date_string: Optional[str] = None):
        if date_string is None:
            timestamp = datetime.now(timezone.utc)
        else:
            timestamp = datetime.fromisoformat(date_string)
            if timestamp.tzinfo is None:
                timestamp = timestamp.replace(tzinfo=timezone.utc)
        self._value = timestamp.astimezone(timezone.utc)

    def __eq__(self, other: "Timestamp") -> bool:
        return self._value == other._value

    def __str__(self) -> str:
        return self._value.strftime("%Y-%m-%d %H:%M:%S")
