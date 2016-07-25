from multiprocessing import Pool, TimeoutError
import time
import os
from datetime import datetime


def f(x):
    return x * x


def f2():
    time.sleep(1.5)
    return os.getpid()


if __name__ == "__main__":
    print("PID:", os.getpid())
    with Pool(processes=4) as pool:
        print(pool.map(f, range(10)))

        for i in pool.imap_unordered(f, range(10)):
            print(i)

        res = pool.apply_async(f, (20,))
        print(res.get(timeout=1))

        res = pool.apply_async(os.getpid, ())
        print(res.get(timeout=1))

        time.sleep(3)

        print(datetime.now())
        multiple_results = [pool.apply_async(f2, ()) for i in range(10)]
        print([res.get(timeout=2) for res in multiple_results])
        print(datetime.now())

        print("Time sleep single process:", datetime.now())
        res = pool.apply_async(time.sleep, (10,))
        try:
            print(res.get(timeout=2))
        except TimeoutError:
            print("We lacked patience")
        print("Time sleep single process:", datetime.now())
    print("Pool is closed")
