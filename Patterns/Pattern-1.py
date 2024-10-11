"""
Pattern:
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4

Things to consider while printing the pattern:
 1. How many rows?
    - The number of rows will be `n`. In this case, `n = 4`.

 2. How many columns?
    - Each row will have `n` columns, where the numbers in each row range from 1 to `n`.

 3. What to print?
    - For each row, print numbers from `1` to `n`.

Breakdown:
    1. The number of rows will be `n`.
    2. The number of columns will be `n`.
    3. For each row, print `j` where `j` starts from 1 and goes up to `n`.
"""

n = 4

for i in range(1, n+1):  # Loop through rows (from 1 to n)
    for j in range(1, n+1):  # Loop through columns: print j from 1 to n
        print(j, end=' ')
    print()  # Move to the next line after each row
