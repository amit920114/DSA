# Multipliction

def mult(m, n):
    if n == 0:
        return 0
    k = mult(m, n-1)
    op = k + m
    return op


print(mult(3, 6))
