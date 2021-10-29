# sum Of arrrays
def sumArr(list, si):
    l = len(list)
    if l == 0 or si == l:
        return 0
    if si == l-1:
        return list[si]
    k = sumArr(list, si+1)
    op = k + list[si]
    return op


kk = [1, 2, 3, 4]
print(sumArr(kk, 0))
