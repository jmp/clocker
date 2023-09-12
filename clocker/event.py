from dataclasses import dataclass, field

from .timestamp import Timestamp


@dataclass(frozen=True)
class ClockedIn:
    timestamp: Timestamp = field(default_factory=Timestamp)


@dataclass(frozen=True)
class ClockedOut:
    timestamp: Timestamp = field(default_factory=Timestamp)


Event = ClockedIn | ClockedOut
