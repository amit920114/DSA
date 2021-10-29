# Finding sum of n nartural numbers:-

def sum_n(n):
    if n == 0:
        return 0
    smallOutput = sum_n(n-1)
    op = smallOutput+n
    return op


# print(sum_n(3))


def _1toN(n):
    if n == 0:
        return
    _1toN(n-1)
    print(n)
    return ""


ll = _1toN(6)
# print(ll)

# print n to 1


def nto1(n):
    if n == 0:
        return
    print(n)
    nto1(n-1)
    return ""


jj = nto1(6)
# print(jj)

# Fibonnaci Series


def fibo(n):
    if n == 1 or n == 2:
        return 1
    k = fibo(n-1)
    p = fibo(n-2)
    return k+p


bb = fibo(5)
# print(bb)

# Check if list is Sorted or Not


def sort(list, n):
    l = len(list)
    if n == l or n == l-1:
        return True
    if list[n] > list[n+1]:
        return False
    smallOp = sort(list, n+1)
    return smallOp


oo = [1, 9, 3, 4]
# print(sort(oo, 0))

# 2nd Way


def sort2(list):
    length = len(list)
    if length == 0 or length == 1:
        return True
    if list[0] > list[1]:
        return False
    smallOp = sort2(list[1:])
    return smallOp


print(sort2(oo))
