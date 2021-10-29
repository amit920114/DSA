# MultiThreading
from threading import Thread, Lock
import time

databse_val = 0


def increase(lock):
    with lock:
        global databse_val
        local_copy = databse_val
        local_copy += 1
        time.sleep(0.1)  # heres switing bw thread goes on
        databse_val = local_copy


if __name__ == "__main__":

    lock = Lock()
    print("Satrt Value", databse_val)
    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    # Starting thread
    thread1.start()
    thread2.start()

    # Join Thread

    thread1.join()
    thread2.join()

    print("End Value", databse_val)
    print("END Main")
