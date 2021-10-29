from threading import Thread, Lock, current_thread
from queue import Queue


def worker(q, lock):
    while True:
        value = q.get()
        with lock:
            print(f"in {current_thread().name} get {value}")
        q.task_done()


if __name__ == "__main__":
    q = Queue()
    num_thread = 10

    lock = Lock()

    for k in range(num_thread):
        thread = Thread(target=worker, args=(q, lock))
        thread.daemon = True
        thread.start()

    # fill the ques

    for l in range(20):
        q.put(l)

    q.join()
    print("End Main")
