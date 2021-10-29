# Binary Search Using Recursion

def binarySearch(list, si, ei, x):
    if si > ei:
        return -1
    mid = (si+ei)//2
    if list[mid] == x:
        return mid
    elif list[mid] > x:
        return binarySearch(list, si, mid-1, x)
    else:
        return binarySearch(list, mid+1, ei, x)


kk = [1, 2, 3, 4, 5, 11, 13, 15, 17]
print(binarySearch(kk, 0, 8, 18))
