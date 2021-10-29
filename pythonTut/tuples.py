# Tuples:- Tuples are similar to lists but not same. Tuples are written in (), and they are immutable.
# It takes less time to execute and takes less storage in comoparison with Lists

import timeit
import sys
my_tuple = "Amit", "Suresh", "Saina", "Lovely"
my_tuple2 = ("Amit", "Suresh", "Saina", "Lovely")
my_tuple3 = ("Ajay")  # this is string type

print(type(my_tuple3))
my_tuple4 = ("sadhvi",)
print(type(my_tuple4))
print("*"*20)
print("\n")
print(my_tuple)
# print(my_tuple2)
# print(my_tuple3)
# Tuples are iterable
for z in my_tuple:
    print(z)
print("*"*20)
if "Amit" in my_tuple:
    print("Yes")
else:
    print("no")

print("*"*20)

if "Laila" in my_tuple:
    print("Yes")
else:
    print("No")
print("*"*20)
print(my_tuple)
print("*"*20)
print(len(my_tuple))
print("*"*20)

print(my_tuple.count("Amit"))
print("*"*20)

print(my_tuple.index("Saina"))

tuple_to_list = list(my_tuple)
print(tuple_to_list)

mylist = ["Pankanj", "Ladu", "Narin", "Geeta"]
list_to_tuple = tuple(mylist)
print(list_to_tuple)
print("*"*20)
print("*"*20)
print(my_tuple)

# Slicing is also done in Tuples:-
print(my_tuple[::2])

# UnPacking in Tuples:-
print("*"*20)
print("*"*20)
new_tuple = (1, 2, 3, "Anil", 4)


z1, *z2, z3, z4 = new_tuple
print(z1)
print(z2)
print(z3)
print(z4)

print("*"*20)
print("*"*20)
new_tuple1 = (1, 2, 3, 4)

isSquare = [a*a for a in new_tuple1]
print(isSquare)
print("*"*20)
print("*"*20)
print("*"*20)
print("*"*20)
# Testing the time bw Tuples and Lists


tuple_ = (1, 2, 3, "Amit", True)

list_ = [1, 2, 3, "Amit", True]

#
print(sys.getsizeof(tuple_), bytes)
print(sys.getsizeof(list_), bytes)

# In Time
print("*"*20)
print("*"*20)
print("*"*20)
print(timeit.timeit(stmt="(1,2,3,4,5,6,7,789,45)", number=100000))
print(timeit.timeit(stmt="[1,2,3,4,5,6,7,789,45]", number=100000))
