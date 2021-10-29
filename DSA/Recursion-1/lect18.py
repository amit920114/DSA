# Finding last index of element in an Array:-
# Unique
def func(list, si, x):
    l = len(list)
    if l == 0 or l == si:
        return -1
    if list[(l-1)-si] == x:
        return (l-1)-si
    smallList = func(list, si+1, x)
    return smallList


kk = [1, 5, 3, 5, 7, 3, 9, 5, 9, 0, 5, 6, 4, 1, 5, 8, 7, 9, 5, 6, 9, 8]
print(func(kk, 0, 5))
