from abc import ABC, abstractmethod

from ..event import Event


class EventRepository(ABC):
    @abstractmethod
    def save(self, event: Event):
        ...

    @abstractmethod
    def find_last(self) -> Event | None:
        ...
