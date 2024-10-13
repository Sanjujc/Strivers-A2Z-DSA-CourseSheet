def digit_count(n):
    n = abs(n)  # Use abs to handle negative numbers
    n_str = str(n)
    count = 0
    for x in n_str:
        digit = int(x)  # Convert character back to an integer
        if digit != 0 and n % digit == 0:  # Check if the digit is not zero and is a divisor
            count += 1

    return count


# Example usage
number = 2446
count = digit_count(number)
print(f"The number of digits in {number} is: {count}")
