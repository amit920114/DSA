# Equilibrium index of an array


def equi(arr, n):
    for i in range(0, n):
        leftSum = 0
        rightSum = 0
        for k in range(i):
            leftSum += arr[k]
        for j in range(i + 1, n):
            rightSum += arr[j]
        if leftSum == rightSum:
            return i
    return -1


def equi2(arr, n):
    rightSum = sum(arr)
    leftSum = 0
    for i, num in enumerate(arr):
        rightSum -= num
        if leftSum == rightSum:
            return i
        leftSum += num
    return -1


arr = [11, 10, 13, 12, 5, 5, 15, 2, 3, 15, 6]
# arr = [-7, 1, 5, 2, -4, 3, 0]
print(equi2(arr, 11))
