# -*- coding: utf-8 -*-
import asyncio
from datetime import datetime


async def display_date(loop):
    end_time = loop.time() + 5.0
    while True:
        print(datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)
    print("Exit while loop")


loop = asyncio.get_event_loop()
loop.run_until_complete(display_date(loop))
loop.close()