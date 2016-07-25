from multiprocessing import Process, Value, Array


def f(num, arr):
    num.value = 101.1
    arr[1] = 2
    arr[3] = 2


if __name__ == "__main__":
    num = Value("d", 0.0)
    arr = Array("i", [1, 1, 1, 1])

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])
