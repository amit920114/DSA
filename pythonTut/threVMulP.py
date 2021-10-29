# Threading V MultiProcessing
from threading import Thread
from multiprocessing import Process
import os


def square_num():
    for i in range(1000):
        i*i


if __name__ == "__main__":
    processes = []
    num_proc = os.cpu_count()

    # Crateing a process

    for i in range(num_proc):
        proc = Process(target=square_num)
        processes.append(proc)

    # Satrt Process
    for p in processes:
        p.start()

    # Join
    for p in processes:
        p.join()
