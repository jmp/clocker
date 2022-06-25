from abc import ABC, abstractmethod

from .event import Event


class EventRepository(ABC):
    @abstractmethod
    def insert_event(self, event: Event):
        ...
