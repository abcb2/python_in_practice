import sys
from . import Event


class NullHandler:
    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, event):
        if self.__successor is not None:
            self.__successor.handle(event)


class DebugHandler(NullHandler):
    def __init__(self, successor=None, file=sys.stdout):
        super().__init__(successor)
        self.__file = file

    def handle(self, event):
        self.__file.write("*DEBUG*: {}\n".format(event))
        super().handle(event)


class MouseHandler(NullHandler):
    def handle(self, event):
        if event.kind == Event.MOUSE:
            print("Click: {}".format(event))
        else:
            super().handle(event)


class KeyHandler(NullHandler):
    def handle(self, event):
        if event.kind == Event.KEYPRESS:
            print("Press: {}".format(event))
        else:
            super().handle(event)


class TimerHandler(NullHandler):
    def handle(self, event):
        if event.kind == Event.TIMER:
            print("Timeout: {}".format(event))
        else:
            super().handle(event)
