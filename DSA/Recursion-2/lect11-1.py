# Quick Sort Decending Order

def partition(list, si, ei):
    pivot = list[si]
    # no of values count krenge
    c = 0
    for k in range(si, ei+1):
        if pivot < list[k]:
            c += 1
    list[si], list[si+c] = list[si+c], list[si]
    pivot_index = si+c

    i = si
    j = ei

    while i < j:
        if pivot < list[i]:
            i += 1
        elif pivot > list[j]:
            j -= 1
        else:
            list[i], list[j] = list[j], list[i]
    return pivot_index


def quick_sort(list, si, ei):
    if si >= ei:
        return
    pivot_index = partition(list, si, ei)
    quick_sort(list, si, pivot_index-1)
    quick_sort(list, pivot_index+1, ei)
    return list


kk = [4, 2, 5, 1, 6, 3, 7]
print(quick_sort(kk, 0, 6))
