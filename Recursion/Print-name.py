def printNos(name,n):
    if n == 0:
        return
    printNos(name,n - 1)
    print(name)

(printNos('Sanju',10))