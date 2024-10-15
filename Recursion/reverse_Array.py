def revArray(arr):
    if not arr:
        return []

    return [arr[-1]] + revArray(arr[:-1])


print(revArray([1,4,5,6,7,7]))

