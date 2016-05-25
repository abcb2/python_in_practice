# -*- coding: utf-8 -*-
import logging
from lib.counter import Counter
from lib.event import Event
from lib.multiplexer import Multiplexer
import random

logging.basicConfig(level=logging.INFO)

random.seed(777)


def generate_random_events(count):
    vehicles = (("cars",) * 11) + (("vans",) * 3) + ("trucks",)
    for _ in range(count):
        yield Event(random.choice(vehicles), random.randint(1, 3))


totalCounter = Counter()
carCounter = Counter("cars")
commercialCounter = Counter("vans", "trucks")

multiplexer = Multiplexer()
for event_name, callback in (
        ("cars", carCounter),
        ("vans", commercialCounter),
        ("trucks", commercialCounter)):
    multiplexer.connect(event_name, callback)
    multiplexer.connect(event_name, totalCounter)

for event in generate_random_events(100):
    multiplexer.send(event)

logging.info(
    "After 100 active events: cars={} vans={} trucks={} total={}".format(
        carCounter.cars, commercialCounter.vans,
        commercialCounter.trucks, totalCounter.count)
)

multiplexer.state = Multiplexer.DORMANT
for event in generate_random_events(100):
    multiplexer.send(event)

logging.info(
    "After 100 active events: cars={} vans={} trucks={} total={}".format(
        carCounter.cars, commercialCounter.vans,
        commercialCounter.trucks, totalCounter.count)
)

multiplexer.state = Multiplexer.ACTIVE
for event in generate_random_events(100):
    multiplexer.send(event)

logging.info(
    "After 100 active events: cars={} vans={} trucks={} total={}".format(
        carCounter.cars, commercialCounter.vans,
        commercialCounter.trucks, totalCounter.count)
)

