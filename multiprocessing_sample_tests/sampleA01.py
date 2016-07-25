from multiprocessing import Pool
from datetime import datetime
import time


def f(x):
    time.sleep(2)
    return x * x


if __name__ == "__main__":
    print(datetime.now())

    with Pool(5) as p:
        print(p.map(f, [1, 2, 3, 4, 5, 6, 7]))

    print(datetime.now())
