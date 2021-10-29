from multiprocessing import Process
import time
from multiprocessing import Queue


def square(que, num):
    for k in num:
        que.put(k*k)


def negative(que, num):
    for k in num:
        que.put(k*-1)


if __name__ == "__main__":

    q = Queue()
    number = range(1, 6)
    p1 = Process(target=square, args=(q, number))
    p2 = Process(target=negative, args=(q, number))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    while not q.empty():
        print(q.get())

    print("End Main")
