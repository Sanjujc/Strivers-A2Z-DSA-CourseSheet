def rotate_n_place(arr, place):
    temp = arr[:place]
    print(temp)
    if len(arr) ==0:
        return None
    for each in range(len(arr)-1):
        arr[each] = arr[each+1]
    arr[-1] = temp[0]
    return arr
print(rotate_n_place([1, 2, 3, 4, 5], 1))

