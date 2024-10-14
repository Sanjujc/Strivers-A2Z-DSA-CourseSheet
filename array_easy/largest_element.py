from typing import List


def largest(arr: List[int]) -> int:
    # code here
    max_number = 0
    for each in arr:
        max_number = max(max_number, each)

    return max_number
