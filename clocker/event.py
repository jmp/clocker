from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class EventType(Enum):
    IN = "IN"
    OUT = "OUT"


@dataclass(frozen=True)
class Event:
    timestamp: datetime
    type: EventType
