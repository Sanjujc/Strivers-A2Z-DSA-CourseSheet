"""
Pattern:
1
1 2
1 2 3
1 2 3 4

Things to consider while printing the pattern:
 1. How many rows?
    - The number of rows will be `n`. In this case, `n = 4`.

 2. How many columns?
    - The number of columns in each row increases:
        - Row 1 has 1 column.
        - Row 2 has 2 columns.
        - Row 3 has 3 columns, and so on, until row `n` has `n` columns.

 3. What to print?
    - In each row, print numbers starting from `1` up to the current row number `i`.

Breakdown:
    1. Number of rows will be `n`.
    2. Number of columns will increase with each row. Row `i` will have `i` columns.
    3. Print `j`, where `j` starts from 1 and goes up to the current row number `i`.
"""

n = 4

for i in range(1, n+1):  # Loop through rows (from 1 to n)
    for j in range(1, i+1):  # Loop through columns: print numbers from 1 to i
        print(j, end=' ')
    print()  # Move to the next line after each row
