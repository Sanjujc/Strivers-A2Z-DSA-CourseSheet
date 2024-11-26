
arr = [11,0,0,1,1,1,2,2,3,3,4]
n = len(arr)
for i in range(1, n):
    if arr[i] < arr[i - 1]:
        print(False)
        break
    else:
        print(True)
        break