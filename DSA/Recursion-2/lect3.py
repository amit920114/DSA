# Replacing pi with 3.14

def func(s):
    if len(s) == 0 or len(s) == 1:
        return s
    if s[0] == 'p' and s[1] == 'i':
        smallOp = func(s[2:])
        return "3.14"+smallOp
    else:
        smallOp = func(s[1:])
        return s[0]+smallOp


ss = "ApiCDp"
print(func(ss))
