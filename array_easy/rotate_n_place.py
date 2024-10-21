def rotate_n_place(arr, place):
    temp = arr[:len(arr)-place]
    print(temp)
    i = 0
    for each in range(place, len(arr)):
        arr[each - place] = arr[each]
        i += 1
    print(arr)
    for each in range(0, len(temp)):
        arr[i] = temp[each]
        i = i + 1
    print(arr)


print(rotate_n_place([1, 2, 3, 4, 5], 4))
