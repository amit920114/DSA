# Segregate 0 and 1


def countZeros(arr, n):
    if len(arr) == 0:
        return
    count = 0
    for k in range(0, n):
        if arr[k] == 0:
            count += 1
    return count


def countOne(arr, n):
    if len(arr) == 0:
        return
    count = 0
    for k in range(0, n):
        if arr[k] == 1:
            count += 1
    return count


data = []


def segregate(arr, n):
    count0 = countZeros(arr, n)
    while count0 > 0:
        data.append(0)
        count0 -= 1
    count1 = countOne(arr, n)
    while count1 > 0:
        data.append(1)
        count1 -= 1
    return data


arr = [1, 0, 1, 0, 0]
print(segregate(arr, 5))
