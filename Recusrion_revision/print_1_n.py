def print_n_to_1(n):
    if n == 0:
        return
    x = n -1
    print_n_to_1(x)
    print(n)
print_n_to_1(3)