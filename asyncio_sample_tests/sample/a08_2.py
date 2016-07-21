# -*- coding: utf-8 -*-
import asyncio
from datetime import datetime


async def sample_task(name, num):
    await asyncio.sleep(num)
    print("Task %s sleep %s" % (name, num))


print(datetime.now())
loop = asyncio.get_event_loop()
tasks = [
    asyncio.ensure_future(sample_task("A", 1)),
    asyncio.ensure_future(sample_task("B", 1)),
    asyncio.ensure_future(sample_task("C", 1)),
]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
print(datetime.now())
