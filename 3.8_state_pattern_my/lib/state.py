class Active:
    def __init__(self):
        pass

    def connect(self, callbacksForEvent, event_name, callback):
        callbacksForEvent[event_name].append(callback)

    def disconnect(self, *args):
        pass

    def send(self, callbacksForEvent, event):
        for callback in callbacksForEvent.get(event.name, ()):
            callback(event)


class Dormant:
    def __init__(self, *args):
        pass

    def connect(self, *args):
        pass

    def disconnect(self, *args):
        pass

    def send(self, *args):
        pass
