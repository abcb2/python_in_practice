from lib.multiplexer import Multiplexer
from lib.counter import Counter
from lib.event import Event

m = Multiplexer()
carCounter = Counter("cars")

m.connect("cars", carCounter)
event = Event("cars", 2)
m.send(event)
print(carCounter.cars)

m.disable()
m.send(event)
print(carCounter.cars)

m.activate()
m.send(event)
print(carCounter.cars)