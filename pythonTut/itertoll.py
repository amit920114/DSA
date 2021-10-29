# Itertools in python is used tio enhanche the iteration
# Methonds include Product, permutation, combination,accumulate,groupby, infinite iterator
from itertools import cycle, count, repeat
from itertools import groupby
import operator
from itertools import accumulate
from itertools import combinations, combinations_with_replacement
from itertools import permutations
from itertools import product
print("*"*50)
# Used For cartesian Products
var = [1, 2, 3]
var2 = [1, 2]
prod = product(var, var2)
print(list(prod))
# Permutations

permu = permutations(var, 2)
print("*"*50)
print("*"*50)

print((list(permu)))
# Combinations
print("*"*50)
print("*"*50)

var3 = [1, 2, 3, 4, 5]
print(var3)
comb = combinations(var3, 2)
print(list(comb))
print(var3)
comb2 = combinations_with_replacement(var3, 2)
print(list(comb2))
print("*"*50)
print("*"*50)

# GroupBy
print(var3)
acc = accumulate(var3, func=operator.mul)
print(list(acc))
print(list(acc))
print("*"*50)
print("*"*50)

print(var3)

group = groupby(var3, key=lambda x: x < 3)
for key, values in group:
    print(key, list(values))

# Infinite iterator

# Count
print("*"*50)
print("*"*50)

for i in count(10):
    print(i)
    if i == 15:
        break
for i in cycle(var3):
    print(i)

for j in repeat(var3):
    print(j)
