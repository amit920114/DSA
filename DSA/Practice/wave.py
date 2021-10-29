# Wave Like Structure
# [1,2,3,4,5] => [2,1,3,4,5]


def wave(arr, n):
    for k in range(0, n - 1, 2):
        arr[k], arr[k + 1] = arr[k + 1], arr[k]
    return arr


arr = [1, 2, 3]
# print(wave(arr, 2))


def sum(arr, n):
    if len(arr) == 1:
        return arr[0]
    return arr[0] + sum(arr[1:], n)


kk = [1, 2, 3]
print()
# print(sum(arr, 3))
