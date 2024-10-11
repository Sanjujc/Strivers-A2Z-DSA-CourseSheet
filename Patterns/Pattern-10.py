"""
Pattern:
- * * * * * * * * *
- - * * * * * * *
- - - * * * * *
- - - - * * *
- - - - - *

Things to consider while printing the pattern:
 1. How many rows?
    - The number of rows will be `n` (in this case, 5).

 2. How many columns?
    - The number of columns varies:
        - The number of dashes increases as the row number increases.
        - The number of stars (`*`) in each row is calculated using your formula, which is `(n + (n - i) - i) + 1`, where `i` is the current row number.

 3. What to print?
    - For each row, print the required number of `'-'` (dashes) followed by the required number of `'*'` (stars).
    - Dashes: `i` dashes.
    - Stars: `((n + (n - i) - i) + 1)` stars.
"""

n = 50
for i in range(1, n+1):
    # Print the dashes
    for space in range(n-i):
        print('-', end=' ')

    # Print the stars
    for col in range(2*i-1):
        print('*', end=' ')

    # Move to the next line after each row
    print()


for i in range(2, n + 1):
    # Print the dashes
    for space in range(i-1):
        print('-', end=' ')

    # Print the stars using your formula
    for col in range((n + (n - i) - i) + 1):
        print('*', end=' ')

    # Move to the next line after each row
    print()
