n = 36
a = []
for i in range(1, int(n**0.5) + 1):  # Check up to sqrt(n)
    if n % i == 0:
        a.append(i)
        if i != n//i:
            a.append(n//i)


print(a)