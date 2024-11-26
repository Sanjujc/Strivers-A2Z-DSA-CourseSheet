a= [9,8,7,6,5,4,4,3,1]
n = len(a)
def rec_insertion(a,n,index):
    if index ==n:
        return
    j = index-1
    key = a[index]
    while j > -1 and a[j] > key:
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = key
    rec_insertion(a,n,index+1)
    return a
print(rec_insertion(a,n,1
                    ))