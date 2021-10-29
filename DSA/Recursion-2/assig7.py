# Stair Case Problem

def stcase(n):

    if n == 1 or n == 0:
        return 1
    j1 = stcase(n-1)
    j2 = stcase(n-2)
    op = j1 + j2
    return op

   
print(stcase(10))
