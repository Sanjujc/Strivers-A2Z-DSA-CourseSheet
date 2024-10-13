def reverse( x):
    """
    :type x: int
    :rtype: int
    """
    maxInt = 2 ** 31 -1
    minInt = -2 ** 31
    negative =  False
    if x < 0:
        negative = True
    x = abs(x)
    rev = 0
    while x >0:
        rem = x % 10
        rev =  rev * 10 + rem
        x = x // 10
        if rev > maxInt:
            return 0
    if negative:
        rev =  -rev
    if rev < minInt or rev > maxInt:
        return 0
    return rev

print(reverse(5213))

