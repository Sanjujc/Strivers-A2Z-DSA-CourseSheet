
n1 = 9
n2 = 12
gcd = 1
iterator =  min(n1,n2)
for i in range(1,iterator+1):
	if n1%i==0 and n2%i ==0:
		gcd = i
print(gcd)