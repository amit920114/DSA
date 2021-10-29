# Quick Sort

def partion(list, si, ei):
    pivot = list[si]
    # count the no of values which are smaller than pivot
    c = 0
    for k in range(si, ei+1):
        if pivot > list[k]:
            c += 1
    list[si], list[si+c] = list[si+c], list[si]
    pivot_index = c + si
    i = si
    j = ei
    while i < j:
        if list[i] < pivot:
            i += 1
        elif list[j] > pivot:
            j -= 1
        else:
            list[i], list[j] = list[j], list[i]
            i += 1
            j -= 1
    return pivot_index


def quick_sort(list, si, ei):
    if si >= ei:
        return
    pivot_index = partion(list, si, ei)
    quick_sort(list, si, pivot_index-1)
    quick_sort(list, pivot_index+1, ei)
    return list


kk = [5, 7, 2, 1, 4, 3, 6]
print(quick_sort(kk, 0, 6))
