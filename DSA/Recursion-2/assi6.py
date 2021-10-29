# Pair Star
# aa=> a*a
# aaa=>a*a*a
output = ""


def helper(str,  si):
    l = len(str)
    if si == l-1:
        return str

    global output
    output = output+str[si]
    if str[si] == str[si+1]:
        output = output + "*"
        return output
    helper(str, si+1)


def pStar(str):
    l = len(str)
    if l == 0 or l == 1:
        return str
    helper(str,  0)
    return helper


print(pStar("agfh"))
