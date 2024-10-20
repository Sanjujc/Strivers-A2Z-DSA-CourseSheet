def remove_duplicate(arr):
    i = 0
    j = 0
    n = len(arr)
    for each in range(n):
        if arr[i] != arr[j]:
            arr[i+1] = arr[j]
            j = j+1
            i = i+1
        else:
            j = j+1

    return i+1

print(remove_duplicate([1,1,2]))