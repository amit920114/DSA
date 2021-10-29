# Geomatric Sum

def gSum(n):
    if n == 0:
        return 1
    k = gSum(n-1)
    op = k + pow(1/2, n)
    return op


kk = gSum(2)
print(kk)
