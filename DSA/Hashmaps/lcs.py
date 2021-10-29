# Longest Consecutive Path in Array


def lcs(arr, n):
    s = set()
    ans = 0
    for k in arr:
        s.add(k)

    for k in range(n):
        if arr[k] - 1 not in s:

            j = arr[k]
            while j in s:
                j += 1
            ans = max(ans, j - arr[k])

    return ans


arr = [9, 1, 8, 6, 3, 4, 2, 7, 10, 15, 11]
print(lcs(arr, 11))
