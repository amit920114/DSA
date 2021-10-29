# Printing Fibonacci series starting from 1

def fib(x):
    if x == 1 or x == 2:
        return 1
    k = fib(x-1)
    p = fib(x-2)
    op = k+p
    return op


nn = fib(5)
print(nn)
