from datetime import datetime

from clocker.errors import NotClockedInError
from clocker.event import Event, EventType
from clocker.event_repository import EventRepository


class ClockOutUseCase:
    def __init__(self, repository: EventRepository):
        self._repository = repository

    def clock_out(self, timestamp: datetime):
        last_event = self._repository.get_last_event()
        if last_event is None or last_event.type == EventType.OUT:
            raise NotClockedInError()
        event = Event(timestamp, EventType.OUT)
        self._repository.insert_event(event)
