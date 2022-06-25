from datetime import datetime

from clocker.event import Event, EventType
from clocker.event_repository import EventRepository


class ClockInUseCase:
    def __init__(self, repository: EventRepository):
        self._repository = repository

    def clock_in(self, timestamp: datetime):
        event = Event(timestamp, EventType.IN)
        self._repository.insert_event(event)
