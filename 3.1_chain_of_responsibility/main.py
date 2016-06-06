import logging
import lib.Event
from lib.Handler import NullHandler, DebugHandler, KeyHandler, MouseHandler, TimerHandler

logging.basicConfig(level=logging.INFO)

logging.info("Handler Chain #1")
handler1 = TimerHandler(KeyHandler(MouseHandler(NullHandler())))

while True:
    event = lib.Event.next()
    logging.info(event)
    if event.kind == lib.Event.TERMINATE:
        break
    handler1.handle(event)
