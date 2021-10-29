def func(x, n):
    ans = 1
    while n > 0:
        ans = ans*x
        n -= 1
    return ans


l = func(5, 3)
print(l)

#
print("*"*50)
print("*"*50)


def func(n):
    if n == 4:
        return n
    else:
        return 2*func(n+1)


ff = func(-1)
print(ff)
