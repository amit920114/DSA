from multiprocessing import Pool


def func(num):
    return num*num*num


if __name__ == "__main__":

    numbers = range(10)
    p = Pool()
    res = p.map(func, numbers)
    print(res)
    # result = p.apply(func, numbers[0])
    # print(result)
