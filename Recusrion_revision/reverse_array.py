def print_array_reverse(arry, l, r):
    if l > r :
        return
    arry[l], arry[r] = arry[r] ,arry[l]
    print_array_reverse(arry, l + 1, r - 1)
    return arry
arr = [1,2,3,4,6]
print(print_array_reverse(arr,0,len(arr)-1))