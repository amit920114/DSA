# Merge Sort


def merge(list1, list2, list):
    i = 0
    j = 0
    k = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            list[k] = list1[i]
            i += 1
            k += 1
        else:
            list[k] = list2[j]
            j += 1
            k += 1
    # tne below code only run when one of them list will have remaining items
    while i < len(list1):
        list[k] = list1[i]
        i += 1
        k += 1

    while j < len(list2):
        list[k] = list2[j]
        j += 1
        k += 1


def merge_sort(list):
    if len(list) == 0 or len(list) == 1:
        return
    mid = len(list) // 2
    list1 = list[0:mid]
    list2 = list[mid:]
    merge_sort(list1)
    merge_sort(list2)
    merge(list1, list2, list)
    return list


kk = [5, 4, 1, 3, 2]
print(merge_sort(kk))
