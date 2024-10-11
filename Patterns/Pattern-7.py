"""
Pattern:
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1

Things to consider while printing the pattern:
 1. How many rows?
    - The number of rows will be `n` (in this case, 5).

 2. How many columns?
    - The number of columns in each row decreases as the row number increases:
        - Row 1 has `n` columns (i.e., 5 columns).
        - Row 2 has `n - 1` columns (i.e., 4 columns), and so on until row `n`.

 3. What to print?
    - For each row, print the same number (the row number itself) for the required columns.
    - Row `i` prints the number `i` repeated `i` times.
"""

n = 5

for i in range(n, 0, -1):  # Loop for rows starting from n down to 1
    for j in range(1, i+1):  # Loop for columns: each row prints 'i' i times
        print(i, end=' ')
    print()  # Move to the next line
