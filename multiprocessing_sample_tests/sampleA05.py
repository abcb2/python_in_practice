from multiprocessing import Process, Lock

def f_no_lock(i):
    print("hello world", i)

def f_lock(lock, i):
    lock.acquire()
    try:
        print("HELLO WORLD", i)
    finally:
        lock.release()

if __name__ == "__main__":
    for num in range(10):
        Process(target=f_no_lock, args=(num,)).start()

    lock = Lock()
    for num in range(10):
        Process(target=f_lock, args=(lock, num,)).start()

