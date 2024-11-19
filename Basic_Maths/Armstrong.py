def armStrong( x):
    temp = x
    rev = 0
    while x >0:
        rem = x % 10
        rev =  rev +(rem*rem * rem)
        x = x // 10
    if rev == temp:
        return True
    return False
print(armStrong(153))

