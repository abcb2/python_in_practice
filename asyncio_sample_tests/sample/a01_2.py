# -*- coding: utf-8 -*-
import asyncio
import functools


def test(num, loop):
    print("Func test {}".format(num))
    loop.stop()


loop = asyncio.get_event_loop()
loop.call_soon(functools.partial(test, num=100, loop=loop))
loop.run_forever()
