def print_sum_n(n,current,s):
    if current > n:
        print(s)
        return
    s = s + current
    print_sum_n(n,current+1,s)

(print_sum_n(4,1,s=0))