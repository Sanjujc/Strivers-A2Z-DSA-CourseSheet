def fact(N):
    if N == 0:
        return 0
    if N == 1:
        return 1
    sum = N *  fact(N - 1)
    return sum

print(fact(3))