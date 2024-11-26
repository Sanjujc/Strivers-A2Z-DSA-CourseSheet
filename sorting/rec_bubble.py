a= [9,8,7,6,5,4,4,3,1]
n = len(a)


def recursion_bubble_sort(a,index):
    if index == n:
        return
    for j in range(0,n-1):
        if a[j] > a[j+1]:
            a[j],a[j + 1]= a[j+1], a[j]
    recursion_bubble_sort(a,index+1)
    return a
print(recursion_bubble_sort(a,0))