# Finding if item is present in list or not
def func(list, n):
    l = len(list)
    if l == 0:
        return False
    if list[0] == n:
        return True
    smallList = list[1:]
    k = func(smallList, n)
    return k


kk = [1, 2, 3]
ff = func(kk, 3)
print(ff)


def func1(list, x, si):
    l = len(list)
    if l == 0 or si == l:
        return False
    if list[si] == x:
        return True
    smallList = func1(list, x, si+1)
    return smallList


print(func1(kk, 3, 3))
