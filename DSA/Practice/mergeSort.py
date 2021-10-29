# Merge Sort


def mergeSort(list):
    if len(list) == 0 or len(list) == 1:
        return
    mid = len(list) // 2
    list1 = list[0:mid]
    list2 = list[mid:]
    mergeSort(list1)
    mergeSort(list2)
    merge(list, list1, list2)
    return list


def merge(list, list1, list2):
    p = 0
    n = 0
    m = 0
    while n < len(list1) and m < len(list2):
        if list1[n] < list2[m]:
            list[p] = list1[n]
            p += 1
            n += 1
        else:
            list[p] = list2[m]
            p += 1
            m += 1
    while n < len(list1):
        list[p] = list1[n]
        n += 1
        p += 1
    while m < len(list2):
        list[p] = list2[m]
        m += 1
        p += 1


list = [5, 1, 4, 2, 3]
print(mergeSort(list))
