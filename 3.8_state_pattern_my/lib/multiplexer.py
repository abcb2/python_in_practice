from .state import Active
from .state import Dormant
from collections import defaultdict


class Multiplexer:
    ACTIVE = Active()
    DORMANT = Dormant()

    def __init__(self):
        self._state = Active()
        self.callbacksForEvent = defaultdict(list)

    @property
    def state(self):
        return self._state

    def activate(self):
        self._state = Multiplexer.ACTIVE

    def disable(self):
        self._state = Multiplexer.DORMANT

    def connect(self, event_name, callback):
        self.state.connect(self.callbacksForEvent, event_name, callback)

    def disconnect(self, event_name, callback=None):
        self.state.disconnect(event_name, callback)

    def send(self, event):
        self.state.send(self.callbacksForEvent, event)
