# Replace X from a String


def func(s, x):
    if len(s) == 0:
        return s
    smallOp = func(s[1:], x)
    if s[0] == x:
        return smallOp
    else:
        return s[0] + smallOp


ss = "BBBBBBBA"
print(func(ss, "B"))
