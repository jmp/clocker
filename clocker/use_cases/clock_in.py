from datetime import datetime

from ..errors import NotClockedOutError
from ..event import Event
from ..action import Action
from ..repositories.event_repository import EventRepository
from ..timestamp import Timestamp


class ClockInUseCase:
    def __init__(self, repository: EventRepository):
        self._repository = repository

    def clock_in(self, timestamp: Timestamp):
        last_event = self._repository.get_last_event()
        if last_event is not None and last_event.action == Action.IN:
            raise NotClockedOutError()

        self._repository.insert_event(Event(timestamp, Action.IN))
