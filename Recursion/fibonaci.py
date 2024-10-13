def fib(s):
    """
    """
    if s == 0:
        return 0
    if s == 1:
        return 1
    fibval = fib(s-1) + fib(s-2)
    return fibval

print(fib(6))