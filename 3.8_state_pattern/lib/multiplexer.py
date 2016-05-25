# -*- coding: utf-8 -*-
import collections


class Multiplexer:
    """
    2つ以上の入力を1つの信号として出力する機構のこと
    DORMANTは「休止」という意味
    """
    ACTIVE, DORMANT = ("ACTIVE", "DORMANT")

    def __init__(self):
        self.callbacksForEvent = collections.defaultdict(list)
        self.state = Multiplexer.ACTIVE

    def connect(self, event_name, callback):
        if self.state == Multiplexer.ACTIVE:
            self.callbacksForEvent[event_name].append(callback)

    def send(self, event):
        if self.state == Multiplexer.ACTIVE:
            for callback in self.callbacksForEvent.get(event.name, ()):
                callback(event)
