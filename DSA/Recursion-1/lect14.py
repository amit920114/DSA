# Is given Array Sorted or Not:-  Better Way

def func(list, n):
    l = len(list)
    if n == l or n == l-1:
        return True
    if list[n] > list[n+1]:
        return False
    smallList = func(list, n+1)
    return smallList


kk = [8, 5]
print(func(kk, 0))
