# Random Numbers

import numpy as np
import secrets
import random
a = random.random()
print("*"*50)
print(a)
print("*"*50)
# random.uniform(2parm) can generate values in bw tp numbers 2nd args is excluded
print(random.uniform(1, 5))
print("*"*50)
print("*"*50)
# randint can include their 2nd param
print(random.randint(1, 5))
print("*"*50)
# randrange can exclude the 2nd parm and give an integer
print(random.randrange(1, 5))

print("*"*50)
# Sigma and miu
print("*"*50)
print(random.normalvariate(1, 5))
print("*"*50)
print("*"*50)
print("on Lists")
mylist = list("ABCDEFGH")
# print()
print("*"*50)
# Choices give an array
# and choice gives a signle srting
print(random.choices(mylist))
print(random.choice(mylist))
print("*"*50)
# .sample can't repeat values choices does
print(random.sample(mylist, 2))
print("*"*50)
print(random.choices(mylist, k=2))
print(random.choices(mylist, k=3))
print(random.shuffle(mylist))
print("*"*50)
print("*"*50)
print("SEEDS")
# seeds can randomly pick a value and doest alter that
# Not used for security purposes
print("*"*50)
print("*"*50)
print("*"*20, "SEED", "*"*50)
random.seed(1)
print(random.random())
print(random.randint(1, 10))

random.seed(2)
print(random.random())
print(random.randrange(1, 10))

random.seed(1)
print(random.random())
print(random.randrange(1, 10))

random.seed(2)
print(random.random())
print(random.randrange(1, 10))

random.seed(3)
print(random.random())
print(random.randrange(1, 10))

random.seed(3)
print(random.random())
print(random.randrange(1, 10))
print("*"*50)
print("*"*50)
# For security purposes we use Secrets functions
b = secrets.randbelow(10)
print(b)
print("*"*50)
# included last one
print(secrets.randbits(4))

# Numpy

print("*"*15, "NUMPY", "*"*15)
print("*"*15, "NUMPY", "*"*15)
print("*"*15, "NUMPY", "*"*15)
# can give a list
s = np.random.rand(3)
j = np.random.rand(3, 3)

print(s)
print("*"*50)
print(j)
# randint

print("*"*50)
print("*"*50)

# print(np.randint(0, 10))
g = np.random.randint(1, 10, (4, 5))
print(g)


print("*"*50)
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(arr)
np.random.shuffle(arr)
print(arr)

print("*"*50)

np.random.seed(1)
print(np.random.random())
print("*"*50)
np.random.seed(2)
print("*"*50)
print(np.random.random())
np.random.seed(1)
print("*"*50)
print(np.random.random())
print("*"*50)
np.random.seed(2)
print(np.random.random())
