from abc import ABC, abstractmethod
from typing import Optional

from clocker.event import Event


class EventRepository(ABC):
    @abstractmethod
    def insert_event(self, event: Event):
        ...

    @abstractmethod
    def get_last_event(self) -> Optional[Event]:
        ...
