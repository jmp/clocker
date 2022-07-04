from datetime import datetime

from ..errors import NotClockedInError
from ..event import Event
from ..action import Action
from ..repositories.event_repository import EventRepository


class ClockOutUseCase:
    def __init__(self, repository: EventRepository):
        self._repository = repository

    def clock_out(self, timestamp: datetime):
        last_event = self._repository.get_last_event()
        if last_event is None or last_event.action == Action.OUT:
            raise NotClockedInError()

        self._repository.insert_event(Event(timestamp, Action.OUT))
