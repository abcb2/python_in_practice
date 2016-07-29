from multiprocessing import Pool
import multiprocessing
import time
from datetime import datetime, timedelta
from pprint import pprint


class Worker(object):
    def __init__(self):
        pass

    @staticmethod
    def process_job(i):
        time.sleep(0.5)
        calc_result = i * i
        pid = multiprocessing.current_process().pid
        mess = "OK"

        try:
            raise Exception("hoge")
        except Exception as e:
            mess = e
        return {"pid": pid, "result": calc_result, "mess": mess}

    def start(self):
        for _ in range(10):
            p = multiprocessing.Pool()
            for result in p.imap_unordered(Worker.process_job, [1, 2, 3]):
                print(result)
            p.close()
            p.join()


if __name__ == "__main__":
    worker = Worker()
    worker.start()
