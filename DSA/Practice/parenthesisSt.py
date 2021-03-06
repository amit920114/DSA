# Check if Parenthesis is Balanced or Not:


def balancedParenthesis(str):
    s = []
    for k in str:
        if k in "{[(":
            s.append(k)
        elif k == ")":
            if not s or s[-1] != "(":
                return False
            s.pop()
        elif k == "]":
            if not s or s[-1] != "[":
                return False
            s.pop()
        elif k == "}":
            if not s or s[-1] != "{":
                return False
            s.pop()
    if not s:
        return True
    else:
        return False


# print(balancedParenthesis("{4)}"))


def isBalanced(str):
    s = []
    for char in str:
        if char in "([{":
            s.append(char)
        elif char == ")":
            if not s or s[-1] != "(":
                return False
            s.pop()
        elif char == "}":
            if not s or s[-1] != "{":
                return False
            s.pop()
        elif char == "]":
            if not s or s[-1] != "[":
                return False
            s.pop()
    if not s:
        return True
    else:
        return False


print(isBalanced("{a+b*(452+[456]}"))
