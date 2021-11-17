# Rotate Array from a given Distance:-


def rotate(arr, n, d):
    if len(arr) == 0 or len(arr) == 1:
        return
    if d <= 0:
        return
    data = []
    for i in range(d):
        data.append(arr.pop(0))

    for i in range(len(data)):
        arr.append(data.pop(0))
    return arr


arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# print(rotate(arr, 10, 3))


def rotateV2(arr, n, d):
    for i in range(d):
        leftRotateByOne(arr, n)
    return arr


def leftRotateByOne(arr, n):
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp


print(rotateV2(arr, 10, 3))
