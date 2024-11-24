def print_n_to_1(n):
    if n == 0:
        return
    x = n -1
    print(n)
    print_n_to_1(x)
print_n_to_1(10)