def check_sorted(nums):
    count = 0
    for each in range(1, len(nums)):
        if nums[each] < nums[each - 1]:
            count = count + 1
    if nums[-1] > nums[0]:
        count += 1

    return count <=1
print(check_sorted([6,3,4,5,1,2]))