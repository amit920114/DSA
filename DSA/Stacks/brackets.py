# Check if Brackets are balanced or Not

import queue


def isBalanced(string):

    s = []
    for char in string:
        if char in "([{":
            s.append(char)
        elif char is ")":
            if not s or s[-1] != "(":
                return False
            s.pop()
        elif char is "]":
            if not s or s[-1] != "[":
                return False
            s.pop()
        elif char is "}":
            if not s or s[-1] != "{":
                return False
            s.pop()
    if not s:
        return True
    else:
        return False


s = input()
print(isBalanced(s))
