# Replace a with b in a String

def func(s, a, b):
    if len(s) == 0:
        return s
    smallOutput = func(s[1:], a, b)
    if s[0] == a:
        return b + smallOutput
    else:
        return s[0] + smallOutput


kk = "ABCDBE"
print(func(kk, "B", "X"))
