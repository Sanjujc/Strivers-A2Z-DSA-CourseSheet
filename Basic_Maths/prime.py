n = 11
counter = 0
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        counter += 1
        if n // i != i:
            counter += 1
        if counter > 2:  # Optimization: Stop early if more than 2 divisors
            break

if counter == 2:
    print('Yes it is a prime')
else:
    print('No, it is not a prime')
