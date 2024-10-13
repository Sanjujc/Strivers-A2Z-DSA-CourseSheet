"""
Pattern:
*
**
***
****
*****
****
***
**
*

Things to consider while printing the pattern:
 1. How many rows?
    - The number of rows will be `2n - 1` (since there are 5 increasing rows and 4 decreasing rows, totaling 9 rows).

 2. How many columns?
    - The number of columns varies:
        - In the first half, the number of stars (`*`) increases from 1 to `n`.
        - In the second half, the number of stars (`*`) decreases from `n-1` to 1.

 3. What to print?
    - For the first `n` rows, print `i` stars (`*`), where `i` is the current row number.
    - For the next `n-1` rows, print `i` stars (`*`), where `i` decreases as you move down the rows.
"""

n = 5

# First part: increasing pattern
for row in range(1, n + 1):
    for col in range(row):
        print('*', end='')
    print()

# Second part: decreasing pattern
for row in range(n - 1, 0, -1):
    for col in range(row):
        print('*', end='')
    print()
