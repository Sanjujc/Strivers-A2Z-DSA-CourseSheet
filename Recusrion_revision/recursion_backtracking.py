
def bt_print_n_to_1(n,current):
	if current > n:
		return 0
	bt_print_n_to_1(n,current+1)
	print(current)

bt_print_n_to_1(5,1)