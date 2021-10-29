# Recursion :

# Step-1 give it initail value or prove it for 1
# Step-2 Induction Hypothesis (Assumption)
# Step-3 Prove it for n+1

# Finding factorial n

from os import X_OK


def fact(n):
    if n == 1:
        return 1
    k = fact(n-1)
    op = n*k
    return op


n = int(input("Enter the number:-  "))
# print(fact(n))

# Finding sum of first n natural numbers


def sum_N(n):
    if n == 1:
        return 1
    k = sum_N(n-1)
    op = n + k
    return op


# print(sum_N(n))


# Printing first N numbers

def _1toN(n):
    if n == 0:
        return
    _1toN(n-1)
    print(n)
    return ""


oo = _1toN(n)
print(oo)

print("#"*50)
# Printing n to 1


def nto1(n):
    if n == 0:
        return
    print(n)
    nto1(n-1)
    return ""


hh = nto1(n)
print(hh)
