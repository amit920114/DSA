# Printing First N natural Numbers


def firstN(n):
    if n == 0:
        return 0
    firstN(n - 1)
    return print(n)


# firstN(5)

# Fibonacci Numbers


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    else:
        return fibo(n - 1) + fibo(n - 2)


# print(fibo(9))

# Sum of Arrays


def sumArr(list, si=0):
    l = len(list)
    if l == 0 or si == l:
        return 0
    if l == 1:
        return list[si]
    return sumArr(list, si + 1) + list[si]


print(sumArr([4, 2, 1, 5]))
