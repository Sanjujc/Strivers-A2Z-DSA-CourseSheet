def factor_n(n):
    if n == 1:
        return 1
    return n * factor_n(n - 1)

print(factor_n(5))