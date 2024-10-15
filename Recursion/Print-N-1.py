def printNos(N):
    if N == 0:
        return 0
    if N == 1:
        return 1
    sum = N + printNos(N - 1)
    return sum

print(printNos(3))