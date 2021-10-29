# Threads in Python
from threading import Thread
# import time


def square_num():
    for o in range(1000):
        o*o


if __name__ == "__main__":
    threads = []
    thread_num = 10

    # making of thraed
    for k in range(thread_num):
        thread = Thread(target=square_num)
        threads.append(thread)

    # start thread
    for t in threads:
        t.start()

    # Join
    for t in threads:
        t.join()
