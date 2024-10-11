"""
Pattern:
* * * * *
* * * *
* * *
* *
*

Things to consider while printing the pattern:
 1. How many rows?
    - The number of rows will be `n + 1` (since you want `n` plus an additional row for the complete pattern).
    - In this case, for `n = 4`, the total number of rows will be `5`.

 2. How many columns?
    - The number of columns in each row decreases:
        - Row 1 has `n + 1` columns (i.e., 5 stars).
        - Row 2 has `n` columns (i.e., 4 stars), and so on until row `n + 1` has `1` column.

 3. What to print?
    - Print `*` followed by a space for each column.
    - The number of stars decreases as the row number increases.
"""

n = 4

for i in range(n + 1, 0, -1):  # Loop for rows starting from n+1 down to 1
    for j in range(1, i):      # Loop for columns: print '*' i times in each row
        print('*', end=' ')
    print()  # Move to the next line after each row
