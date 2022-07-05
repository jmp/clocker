from dataclasses import dataclass

from .action import Action
from .timestamp import Timestamp


@dataclass(frozen=True)
class Event:
    timestamp: Timestamp
    action: Action
