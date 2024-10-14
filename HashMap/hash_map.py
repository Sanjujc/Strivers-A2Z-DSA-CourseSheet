def frequencyCount(arr, N, P):
    hash_arr = [0] * int(N + 1)
    print(hash_arr)
    for each in arr:
        if hash_arr[each] == 0:
            hash_arr[each] =1
        else:
            hash_arr[each] +=1
    return hash_arr
n = 5
arr = [2, 3, 2, 3, 5]
p = 5
print(frequencyCount(arr,n,p))