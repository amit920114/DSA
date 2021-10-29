# Palindrome Checker
# abcba is True

def helper(s, si, ei):
    if si == ei:
        return True
    if s[si] != s[ei]:
        return False
    if si < ei+1:
        return helper(s, si+1, ei-1)
    return True


def isPalindrome(string):
    l = len(string)
    if l == 0:
        return True
    return helper(string, 0, l-1)


print(isPalindrome("abcbaa"))
