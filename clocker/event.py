from dataclasses import dataclass, field

from .action import Action
from .timestamp import Timestamp


@dataclass(frozen=True)
class Event:
    action: Action
    timestamp: Timestamp = field(default_factory=Timestamp)


@dataclass(frozen=True)
class InEvent(Event):
    action: Action = field(init=False, default=Action.IN)


@dataclass(frozen=True)
class OutEvent(Event):
    action: Action = field(init=False, default=Action.OUT)
