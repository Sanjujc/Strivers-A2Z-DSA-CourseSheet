a= [9,8,7,6,5,4,4,3,1]
n = len(a)
for i in range(0, n - 1):
    min = i
    for j in range(i, n):
        if a[j] < a[min]:
            min = j
    a[i], a[min] = a[min], a[i]
print(a)