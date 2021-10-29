# Sum of all elements in an Array
def func(list):
    l = len(list)
    if l == 0:
        return 0
    smallList = list[1:]
    assum = func(smallList)
    op = list[0] + assum
    return op


kk = [1, 2, 3, 5, 11]
pp = func(kk)
print(pp)


def func1(list, si):
    l = len(list)
    if l == 0 or si == l:
        return 0
    if si == l-1:
        return list[si]
    smallList = func1(list, si+1)
    op = smallList + func1(list, si)
    return op


print(func1(kk, 0))
