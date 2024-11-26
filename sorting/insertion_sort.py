a= [9,8,7,6,5,4,4,3,1]
n = len(a)

for i in range(1,n):
    j = i - 1
    key = a[i]
    while j >-1 and a[j] > key:
        a[j+1] = a[j]
        j -=1
    a[j+1] = key
print(a)

