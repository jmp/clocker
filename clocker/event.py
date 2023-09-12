from dataclasses import dataclass, field

from .action import Action
from .timestamp import Timestamp


@dataclass(frozen=True)
class InEvent:
    timestamp: Timestamp = field(default_factory=Timestamp)
    action = Action.IN


@dataclass(frozen=True)
class OutEvent:
    timestamp: Timestamp = field(default_factory=Timestamp)
    action = Action.OUT


Event = InEvent | OutEvent
