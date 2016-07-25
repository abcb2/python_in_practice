import multiprocessing as mp
import os


def foo(q):
    print("In foo pid:{}".format(os.getpid()))
    q.put("hello")


if __name__ == "__main__":
    mp.set_executable("spawn")
    q = mp.Queue()
    p = mp.Process(target=foo, args=(q,))
    p.start()
    print("In main pid:{}".format(os.getpid()))
    print(q.get())
    p.join()
