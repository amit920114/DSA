# Sum of Array's


def sumArr(arr, n):
    if len(arr) == 1:
        return arr[0]
    return arr[0] + sumArr(arr[1:], n)


def sumLoop(arr, n):
    sum = 0
    for k in range(0, n):
        sum = sum + arr[k]
    return sum


arr = [1, 2, 3, 4, 10, 6]
# print(sumArr(arr, 3))

# print(sum(arr))
print(sumLoop(arr, 6))
