from types import NoneType

from ..errors import NotClockedInError
from ..event import OutEvent
from ..repositories.event_repository import EventRepository
from ..timestamp import Timestamp


class ClockOutUseCase:
    def __init__(self, repository: EventRepository):
        self._repository = repository

    def clock_out(self, timestamp: Timestamp):
        last_event = self._repository.get_last_event()
        if isinstance(last_event, (NoneType, OutEvent)):
            raise NotClockedInError()

        self._repository.insert_event(OutEvent(timestamp))
