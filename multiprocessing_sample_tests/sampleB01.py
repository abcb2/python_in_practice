from multiprocessing import Pool
import multiprocessing
import time
from pprint import pprint


def f(i):
    time.sleep(2)
    calc_result = i * i
    pid = multiprocessing.current_process().pid
    return {"pid": pid, "result": calc_result}


if __name__ == "__main__":
    for x in [1, 2]:
        _task_num = 5 * x
        with Pool(_task_num) as p:
            results = p.map(f, [i for i in range(_task_num)])
            pprint(results)
