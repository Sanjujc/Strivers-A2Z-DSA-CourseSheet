"""
Pattern:
*
* *
* * *
* * * *

Things to consider while printing the pattern:
 1. How many rows?
    - The number of rows will be `n`. In this case, `n = 4`.

 2. How many columns?
    - The number of columns in each row increases with the row number:
        - Row 1 has 1 column.
        - Row 2 has 2 columns.
        - Row 3 has 3 columns, and so on until row `n` has `n` columns.

 3. What to print?
    - Print asterisks (`*`) in each row, with the number of asterisks increasing in each row.

Breakdown:
    1. The number of rows will be `n`.
    2. The number of columns in each row will be equal to the row number `i`.
    3. Print `*` for each column.
"""

n = 4

for i in range(1, n+1):  # Loop through rows (from 1 to n)
    for j in range(1, i+1):  # Loop through columns: print '*' i times in each row
        print('*', end=' ')
    print()  # Move to the next line after each row
