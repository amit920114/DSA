# Check if list is sorted or not


def sort(list, si):
    l = len(list)
    if si == l - 1 or si == l:
        return True
    if list[si] > list[si + 1]:
        return False

    return sort(list, si + 1)


# print(sort([1, 2, 7, 4], 0))

# First index of Element


def index(list, x, si=0):
    l = len(list)
    if si == l:
        return -1
    if list[si] == x:
        return si
    return index(list, x, si + 1)


# print(index([1, 2, 3, 5, 7, 3, 5], 5))

# Check If element is Present or not


def present(list, x, si=0):
    l = len(list)
    if si == l:
        return False
    if list[si] == x:
        return True
    return present(list, x, si + 1)


# print(present([1, 2, 3, 5, 7, 3, 5], 99))

# Last Index of element in an array
def lastIndex(list, l, x):
    if l == 0:
        return -1
    if list[l - 1] == x:
        return l - 1
    return lastIndex(list, l - 1, x)


# print(lastIndex([1, 2, 3, 5, 2, 7, 4, 7, 3, 5], 10, 2))

# Given a string, compute recursively a new string where all 'x' chars have been removed.


def removeX(str, si, x):
    l = len(str)
    if si == l:
        return ""
    if str[si] == x:
        return removeX(str, si + 1, x)
    return str[si] + removeX(str, si + 1, x)


print(removeX("xAxBxCxD", 0, "x"))
