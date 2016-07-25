import multiprocessing
import time
import signal
import os


def get_job():
    return range(6)


def process_task(job):
    pid = multiprocessing.current_process().pid
    print("pid:{}, job:{}".format(pid, job))
    time.sleep(1)
    return "JOB Finished"


def signal_handler(num, frame):
    print("Receive Signal", num, "and exit")
    exit(1)


if __name__ == "__main__":

    print("PID:{}".format(os.getpid()))

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    while True:
        print("Begin worker loop")
        with multiprocessing.Pool(10) as pool:
            for job in get_job():
                result = pool.apply_async(process_task, args=(job,))
                print(result.get())
    else:
        print("FINISH")
