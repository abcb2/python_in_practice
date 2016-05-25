# -*- coding: utf-8 -*-
import collections


class Multiplexer:
    ACTIVE, DORMANT = ("ACTIVE", "DORMANT")

    def __init__(self):
        self.callbacksForEvent = collections.defaultdict(list)
        self.state = Multiplexer.ACTIVE

    @property
    def state(self):
        if self.send == self.__active_send:
            return Multiplexer.ACTIVE
        else:
            return Multiplexer.DORMANT

    @state.setter
    def state(self, state):
        if state == Multiplexer.ACTIVE:
            self.connect = self.__active_connect
            self.disconnect = self.__active_disconnect
            self.send = self.__active_send
        else:
            self.connect = lambda *args: None
            self.disconnect = lambda *args: None
            self.send = lambda *args: None

    def __active_connect(self, event_name, callback):
        self.callbacksForEvent[event_name].append(callback)

    def __active_disconnect(self, event_name, callback=None):
        if callback is None:
            del self.callbacksForEvent[event_name]
        else:
            self.callbacksForEvent[event_name].remove(callback)

    def __active_send(self, event):
        for callback in self.callbacksForEvent.get(event.name, ()):
            callback(event)
