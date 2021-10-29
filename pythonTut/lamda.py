# Lamda is defined for inline function
# Syntax:- loamda argument: logic
# Can Take multiple arguments
from functools import reduce
from typing import Mapping


print("*"*50)
var = [1, 2, 3, 4]
def add5(x): return x+5


def mul2(j): return j*2


print(mul2(10))
print("*"*50)
print(add5(5))


def multi(x, y): return x+y


print("*"*50)
print(multi(5, 6))

print("*"*50)

point3D = [(0, 1, 5), (5, 7, 2), (4, 3, 0)]
# Sorted via index 0 by default
print_point2D = sorted(point3D)
print(print_point2D)
# Sorted Via index 1
print_point2D = sorted(point3D, key=lambda x: x[1])

print("*"*50)
print(print_point2D)
print("*"*50)
# Sorted via 2nd Index
print_point2D = sorted(point3D, key=lambda x: x[2])

print(print_point2D)
print("*"*50)
print(point3D)
print_point2D = sorted(point3D, key=lambda x: x[2]+x[0])
print(print_point2D)

# Maping, Filtering, Reduce functions
# Mapping
print("*"*50)
var1 = [1, 2, 3, 4]
maap = map(lambda g: g+2, var1)
# maap = map(var1, lambda g: g+2)
print(var1)
print(list(maap))
print("*"*50)
print("*"*50)
c = [o+2 for o in var1]
print(c)
print("*"*50)
# Filter
fil = filter(lambda x: x < 3, var1)
print(var1)
print(list(fil))
fil2 = filter(lambda f: f % 2 == 0, var1)
d = [d for d in var1 if d % 3 == 0]
print(d)
print(list(fil2))
print("*"*50)
print("*"*50)
# Reduse function can take at least two areguments in a function
print("*"*50)

print(var1)
redu = reduce(lambda x, y: x+y, var1)
print(redu)
