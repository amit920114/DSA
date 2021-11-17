def findExtra(a, b, n):
    # add code here
    for k in range(0, n - 1):
        if a[k] != b[k]:
            return k
        if k == n - 2:
            return n - 1


a = [1, 2, 3, 4]
b = [1, 2, 3]
print(findExtra(a, b, 4))
