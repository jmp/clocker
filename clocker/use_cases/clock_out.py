from datetime import datetime

from clocker.event import Event, EventType
from clocker.event_repository import EventRepository


class ClockOutUseCase:
    def __init__(self, repository: EventRepository):
        self._repository = repository

    def clock_out(self, timestamp: datetime):
        event = Event(timestamp, EventType.OUT)
        self._repository.insert_event(event)
