# A better Way of Doing lect15

def func(list, si, x):
    l = len(list)
    if si == l:
        return -1
    if list[si] == x:
        return si
    k = func(list, si+1, x)
    return k


ll = [1, 2, 3, 4, 3, 5]
# print(func(ll, 1, 3))


# Finding The first index of element

def func1(list, si, x):
    l = len(list)
    if si == l or l == 0:
        return -1
    if list[si] == x:
        return si
    smallList = func1(list, si+1, x)
    return smallList


oo = []
print(func1(oo, 1, 9))
