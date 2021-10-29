# Finding The first index of element

def func(list, x):
    l = len(list)
    if l == 0:
        return -1
    if list[0] == x:
        return 0
    smallList = list[1:]
    k = func(smallList, x)
    if k == -1:
        return -1
    else:
        return k+1


ll = [1, 2, 3, 4, 3, 5]
print(func(ll, 3))
