# Max distance between same elements
def maxDistance(arr, n):
    map = {}
    maxD = 0
    for k in range(n):
        if arr[k] not in map.keys():
            map[arr[k]] = k
        else:
            maxD = max(maxD, k - map[arr[k]])
    return maxD


arr = [1, 1, 2, 2, 2, 1]
print(maxDistance(arr, 6))
