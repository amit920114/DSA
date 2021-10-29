from multiprocessing import Process, Array, Value
from multiprocessing import Lock
import time


def func(number, lock):
    with lock:
        # for k in range(100):
        #     time.sleep(0.01)
        #     number.value += 1
        for _ in range(100):
            for arr in range(len(number)):
                time.sleep(0.01)
                number[arr] += 1



if __name__ == "__main__":

    lock = Lock()
    # square_num = Value("i", 0)
    square_num = Array("d", [0.0, 100.0, 20.00, 300.0])
    # print("Start Value", square_num.value)
    print("Start Value", square_num[:])
    proces1 = Process(target=func, args=(square_num, lock))
    proces2 = Process(target=func, args=(square_num, lock))

    # processing
    proces1.start()
    proces2.start()

    # Join

    proces1.join()
    proces2.join()
    # print("End value", square_num.value)
    print("End Value", square_num[:])
    print("End Main")
