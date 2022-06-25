from datetime import datetime

from ..errors import AlreadyClockedInError
from ..event import Event, EventType
from clocker.repositories.event_repository import EventRepository


class ClockInUseCase:
    def __init__(self, repository: EventRepository):
        self._repository = repository

    def clock_in(self, timestamp: datetime):
        last_event = self._repository.get_last_event()
        if last_event is not None and last_event.type == EventType.IN:
            raise AlreadyClockedInError()

        self._repository.insert_event(Event(timestamp, EventType.IN))
