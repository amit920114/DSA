def gcd(m, n):
    while n:
        m, n = n, m % n
    return m


def gcdArr(arr, n):
    if len(arr) == 0:
        return
    ans = arr[0]
    for i in range(1, n - 1):
        ans = gcd(ans, arr[i])
    return ans


arr = [16, 15, 1]

print(gcdArr(arr, 4))
