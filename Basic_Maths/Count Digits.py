n = 1234
counter = 0
while n > 0:
	digit = n % 10
	counter = counter + 1
	n = n //10
print(counter)