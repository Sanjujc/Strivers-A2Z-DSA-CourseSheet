"""
Pattern:
1
2 2
3 3 3
4 4 4 4

Things to consider while printing the pattern:
 1. How many rows?
    - The number of rows will be `n`. In this case, `n = 4`.

 2. How many columns?
    - The number of columns in each row increases:
        - Row 1 has 1 column.
        - Row 2 has 2 columns, and so on, until row `n` has `n` columns.

 3. What to print?
    - Print the row number `i` repeated `i` times in each row.
"""

n = 4

for i in range(1, n+1):  # Loop through rows (from 1 to n)
    for j in range(1, i+1):  # Loop through columns: print the row number `i` i times
        print(i, end=' ')
    print()  # Move to the next line after each row
