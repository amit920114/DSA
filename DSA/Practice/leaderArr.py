# Find Leader in a Array:-


def leader(arr, n):
    data = []
    data.append(arr[-1])
    temp = arr[-1]
    for k in range(n - 2, -1, -1):
        if arr[k] >= temp:
            data.append(arr[k])
            temp = arr[k]
    data.sort(reverse=True)
    return data


arr = [16, 17, 4, 3, 5, 2]
print(leader(arr, 6))
