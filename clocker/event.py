from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class EventType(Enum):
    IN = 0
    OUT = 1


@dataclass(frozen=True)
class Event:
    timestamp: datetime
    type: EventType
