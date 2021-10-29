# GFG Need To Change


def swapElements(arr, n):
    # Code here
    for i in range(0, n):
        arr[i] = arr[i + 2]
    return arr


arr = [1, 2, 3, 4, 5]

print(swapElements(arr, 5))
