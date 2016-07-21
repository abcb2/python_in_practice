# -*- coding: utf-8 -*-
import asyncio
import signal
import functools
import os


def ask_exit(signame, loop):
    print("got signal %s: exit" % signame)
    loop.stop()


loop = asyncio.get_event_loop()
for signame in ("SIGINT", "SIGTERM"):
    loop.add_signal_handler(
        getattr(signal, signame),
        functools.partial(
            ask_exit, signame=signame, loop=loop
        )
    )

print("Event loop running forever, press Ctrl+C to interrupt.")
print("pid %s: send SIGINT or SIGTERM to exit." % os.getpid())
try:
    loop.run_forever()
finally:
    loop.close()
