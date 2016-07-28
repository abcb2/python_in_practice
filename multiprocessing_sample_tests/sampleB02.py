from multiprocessing import Pool
import multiprocessing
import time
from datetime import datetime, timedelta
from pprint import pprint


def f(i):
    time.sleep(i)
    calc_result = i * i
    pid = multiprocessing.current_process().pid
    return {"pid": pid, "result": calc_result}


if __name__ == "__main__":
    dt_start = datetime.now()
    print("Start:", dt_start)
    with Pool(3) as p:
        results = p.map(f, [1, 2, 3])
        pprint(results)
    dt_end = datetime.now()
    print("End:", dt_end)
    elapsed = dt_end - dt_start
    print("Elapsed:", elapsed.total_seconds())
    print("")

    # map_async
    dt_start = datetime.now()
    print("Start:", dt_start)
    with Pool(3) as p:
        results = p.map_async(f, [1, 2, 3])
        pprint(results.get())
    dt_end = datetime.now()
    print("End:", dt_end)
    elapsed = dt_end - dt_start
    print("Elapsed:", elapsed.total_seconds())
    print("")

    # imap
    dt_start = datetime.now()
    print("Start:", dt_start)
    p = Pool()
    for result in p.imap(f, [1, 3, 2]):
        elapsed = (datetime.now() - dt_start).total_seconds()
        pprint(result)
        pprint(elapsed)
    dt_end = datetime.now()
    print("End:", dt_end)
    elapsed = dt_end - dt_start
    print("Elapsed:", elapsed.total_seconds())
    print("")

    # imap_unordered
    dt_start = datetime.now()
    print("Start:", dt_start)
    p = Pool()
    for result in p.imap_unordered(f, [1, 3, 2]):
        elapsed = (datetime.now() - dt_start).total_seconds()
        pprint(result)
        pprint(elapsed)
    dt_end = datetime.now()
    print("End:", dt_end)
    elapsed = dt_end - dt_start
    print("Elapsed:", elapsed.total_seconds())
    print("")
