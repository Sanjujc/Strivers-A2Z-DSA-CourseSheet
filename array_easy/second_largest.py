
from typing import List


def second_largest(arr: List[int]) -> int:
    second_largest_number = -1
    large_number = arr[0]
    n = len(arr)
    for each in range(1,n):
        if arr[each] > large_number:
            second_largest_number = large_number
            large_number = arr[each]
        elif large_number > arr[each] > second_largest_number:
            second_largest_number =arr[each]
    return second_largest_number

print(second_largest([1,2,8,4,7,6,5]))
