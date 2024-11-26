
def merge_sorted_arry(first_array, second_array, a):
    i = 0
    j = 0
    k = 0
    while i < len(first_array) and j < len(second_array):
        if first_array[i] < second_array[j]:
            a[k] = first_array[i]
            i += 1
            k += 1
        else:
            a[k] = second_array[j]
            j += 1
            k += 1
    while i < len(first_array):
        a[k] = first_array[i]
        i += 1
        k += 1
    while j < len(second_array):
        a[k] = second_array[j]
        j += 1
        k += 1

def merge_sort(a):
    if len(a) <=1:
        return a
    mid_point = len(a) // 2
    first_array = a[0:mid_point]
    second_array = a[mid_point:]

    merge_sort(first_array)
    merge_sort(second_array)
    merge_sorted_arry(first_array, second_array, a)
    return a


print(merge_sort([9,8,7,5,4,3,21,2]))