from clocker.event import Event
from clocker.repositories import EventRepository


class InMemoryEventRepository(EventRepository):
    _inserted_event: Event = None

    def save(self, event: Event):
        self._inserted_event = event

    def find_last(self) -> Event | None:
        return self._inserted_event
