"""
Pattern:
1
01
101
0101
10101

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
    if row % 2 == 0:
        start = 0
    else:
        start = 1
    for col in range(row):
        print(start,end='')
        if start == 1 :
            start =0
        else:
            start =1
    print()

