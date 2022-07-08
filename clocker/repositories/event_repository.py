from abc import ABC, abstractmethod
from typing import Optional

from ..event import Event


class EventRepository(ABC):
    @abstractmethod
    def save(self, event: Event):
        ...

    @abstractmethod
    def find_last(self) -> Optional[Event]:
        ...
