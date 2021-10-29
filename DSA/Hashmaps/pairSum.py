# Pair Sum to 0


def pairSum(arr, n):
    count = 0
    for i in range(0, n):
        for k in range(0, n):
            if arr[i] + arr[k] == 0:
                count += 1
    return count


a = [0] * 10
print(a)
arr = [2, 1, -2, 2, 3, 2]
# print(pairSum(arr, 6))
