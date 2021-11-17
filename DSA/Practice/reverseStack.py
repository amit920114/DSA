# Reverse a Stack Using  another stack


def reverse(s1, s2):
    if len(s1) == 1:
        return
    while len(s1) > 1:
        item = s1.pop()
        s2.append(item)
    lastElem = s1.pop()
    while len(s2) > 0:
        item = s2.pop()
        s1.append(item)
    reverse(s1, s2)
    s1.append(lastElem)
    return s1


arr = [1, 2, 3, 4, 5]
arr2 = []
print(reverse(arr, arr2))
print("Amit")
