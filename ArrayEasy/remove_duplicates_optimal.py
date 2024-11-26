j = 0
i = 0
a = [0,0,1,1,1,2,2,3,3,4]
n = len(a)
for each in range(0, n):
    if a[i] != a[j]:
        a[i + 1] = a[j]
        i = i + 1
        j = j + 1
    else:
        j = j + 1
print(i + 1)
print(a[:i+1])