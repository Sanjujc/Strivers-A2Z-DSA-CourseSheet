a= [9,8,7,6,5,4,4,3,1]
n = len(a)

for i in range(0, n - 1):
    for j in range(0, n-1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print(a)