from typing import Optional

from clocker.event import Event
from clocker.event_repository import EventRepository


class FakeEventRepository(EventRepository):
    def __init__(self):
        self.inserted_event = None

    def insert_event(self, event: Event):
        self.inserted_event = event

    def get_last_event(self) -> Optional[Event]:
        return self.inserted_event
