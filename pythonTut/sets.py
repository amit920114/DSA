# Sets are the unordered collections of data they are mutables and performs sets operations like in MATHS SEts does:-

# mySet = {1, 2, 3, 4}
print("*"*50)
# print(mySet)
mySet = set([1, 2, 3, 4, 5])
print(mySet)
mySet2 = set((1, 2, 5, 7))
print("*"*50)
print("*"*50)
print(mySet2)

mySet.add(6)
mySet.add(7)
mySet.add(8)
mySet.remove(8)
mySet.discard(6)
mySet.pop()
print("*"*50)
print("*"*50)
print(mySet)
for f in mySet:
    print(f)
if 21 in mySet:
    print("yes")
else:
    print("No")
print("*"*50)
print("*"*50)
letters = set("HELLO")
print(letters)
# UNION in Sets
print("*"*50)
print("*"*50)

mySetA = set((1, 2, 3, 4, 5, 6))
mySetB = set((4, 5, 6, 7, 8, 9, 0))
print(mySetA)
print(mySetB)

union = mySetA.union(mySetB)
print(union)
intersection = mySetA.intersection(mySetB)
print("*"*50)
print(intersection)
print("*"*50)
diff = mySetA.difference(mySetB)
print(diff)
print("*"*50)
# Do not take intersected values but merge to sets
sym_diff = mySetA.symmetric_difference(mySetB)
print(sym_diff)
# SET Updates method

# mySetA.update(mySetB)
print("*"*50)
print("*"*50)
# mySetA.intersection_update(mySetB)
# mySetA.difference_update(mySetB)
mySetA.symmetric_difference_update(mySetB)
print(mySetA)
newSetA = set((1, 2, 3, 4, 5))
newSetB = set((1, 2))
print(newSetA.issubset(newSetB))
print(newSetB.issubset(newSetA))
print(newSetB.issuperset(newSetA))
print(newSetA.issuperset(newSetB))
print(newSetA.isdisjoint(newSetB))
# DisJoint sets are those set in which NULL is there common value
print(newSetB.isdisjoint(newSetA))
# To copy a set

u = set(newSetA)
print("*"*50)
print("*"*50)
print(u)
#
# FROZENSET :- these are the sets similar to sets but are not mutables and updation is prohibittes in them
# But Sets relations can be applied on them
