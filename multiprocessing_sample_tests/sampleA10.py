import multiprocessing
import time
from datetime import datetime
from collections import Counter

dt_begin = datetime.now()
finish_delta = 10


def get_jobs():
    dt_now = datetime.now()
    delta = dt_now - dt_begin
    print("Elapsed", float(delta.total_seconds()))
    if delta.total_seconds() > finish_delta:
        return []
    else:
        return [x for x in range(5)]


def process_task(job):
    print("Process Job", job, "PID", multiprocessing.current_process().pid)
    if job == 2:
        raise Exception("ERROR")
    time.sleep(1)


if __name__ == "__main__":
    c = Counter()
    while True:
        jobs = get_jobs()
        if len(jobs) == 0:
            break

        process_list = []
        for job in jobs:
            process_list.append(
                multiprocessing.Process(target=process_task, args=(job,))
            )
        for p in process_list:
            p.start()

        for p in process_list:
            c['total'] += 1
            p.join()

    print("Total ", str(c.most_common()))
