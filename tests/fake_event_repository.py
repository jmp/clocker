from typing import Optional

from clocker.event import Event
from clocker.repositories import EventRepository


class FakeEventRepository(EventRepository):
    def __init__(self, inserted_event: Optional[Event] = None):
        self.inserted_event = inserted_event

    def insert_event(self, event: Event):
        self.inserted_event = event

    def get_last_event(self) -> Optional[Event]:
        return self.inserted_event
