from typing import Optional

from clocker.event import Event
from clocker.repositories import EventRepository


class InMemoryEventRepository(EventRepository):
    def __init__(self, inserted_event: Optional[Event] = None):
        self._inserted_event = inserted_event

    def save(self, event: Event):
        self._inserted_event = event

    def find_last(self) -> Optional[Event]:
        return self._inserted_event
