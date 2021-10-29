# Count No of Zeros:

from typing import Counter

Count = 0


def zeros(n):
    global Count
    if n == 0:
        return 1

    if n > 0:
        if(n % 10 == 0):
            Count += 1
        zeros(n//10)
    return Count


print(zeros(0))
