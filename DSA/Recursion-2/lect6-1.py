# Merge Sort desending order

def merge(list1, list2, list):
    k = 0  # list
    m = 0  # list1
    n = 0  # list2
    while m < len(list1) and n < len(list2):
        if list1[m] > list2[n]:
            list[k] = list1[m]
            m += 1
            k += 1
        else:
            list[k] = list2[n]
            n += 1
            k += 1
 
    while m < len(list1):
        list[k] = list1[m]
        m += 1
        k += 1
    while n < len(list2):
        list[k] = list2[n]
        n += 1
        k += 1


def merge_sort(list):
    if len(list) == 0 or len(list) == 1:
        return
    mid = len(list) // 2
    list1 = list[:mid]
    list2 = list[mid:]
    merge_sort(list1)
    merge_sort(list2)
    merge(list1, list2, list)
    return list


kk = [1, 9, 3, 5, 7, 4]
print(merge_sort(kk))
