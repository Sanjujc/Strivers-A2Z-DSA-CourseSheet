"""
Pattern:
1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4

Things to consider while printing the pattern:
 1. How many rows?
    - The number of rows will be `n`. In this case, `n = 4`.

 2. How many columns?
    - Each row will have `n` columns, where each row prints the same number multiple times.

 3. What to print?
    - In each row, print the row number `i` `n` times.

Breakdown:
    1. The number of rows will be `n`.
    2. Each row will have `n` columns.
    3. Print the row number `i` in each row for all `n` columns.
"""

n = 4

for i in range(1, n+1):  # Loop through rows (from 1 to n)
    for j in range(1, n+1):  # Loop through columns: print the row number i for all n columns
        print(i, end=' ')
    print()  # Move to the next line after each row
