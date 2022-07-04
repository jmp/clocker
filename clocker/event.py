from dataclasses import dataclass
from datetime import datetime

from .action import Action


@dataclass(frozen=True)
class Event:
    timestamp: datetime
    action: Action
