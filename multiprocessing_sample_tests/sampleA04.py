from multiprocessing import Process, Pipe
import os


def foo(conn):
    conn.send([42, None, "Hello"])


if __name__ == "__main__":
    parent_conn, child_conn = Pipe()
    p = Process(target=foo, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    p.join()
