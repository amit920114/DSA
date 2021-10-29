# Given a string S, remove consecutive duplicates from it recursively.

def func(s):
    if len(s) == 0 or len(s) == 1:
        return s
    smallOp = func(s[1:])
    if s[0] == s[1]:
        return smallOp
    else:
        return s[0]+smallOp


ss = "AABCDRRF"
print(func(ss))
