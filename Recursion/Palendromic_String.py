def isPalindrome(s):

    """
    :type s: str
    :rtype: bool
    """
    s = (''.join([x for x in s if x.isalnum()])).lower()
    return s == s[::-1]


s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))