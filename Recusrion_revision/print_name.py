
def print_name(n):
	if n == 0:
		return
	print('Sanju',n)
	x = n -1
	print_name(x)
	print('Sanju',n)
(print_name(4))