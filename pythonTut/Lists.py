# List in Python are like arrays these are placed inside the Square brackets [] and they are mutable unlike
# tuples in Python:

from typing import List


myList = ["Amit", "Ajay", "Anil", "Mukesh", 1, 2, 3, True, False, 5]
# print(myList)

myNewList = list()

myNewList.append("Sunita")
# myNewList.push("Anil")

# print(myList[-1])

# for x in myList:
#     print(x)

# if "Shudhir" in myList:
#     print("yes")
# else:
#     print("No")

# To Check the length

myList.insert(1, "Shudhir")

myList.remove("Shudhir")
# myList.pop(1)
# myList.clear()
# myList.reverse()
# myList.sort()
# print(myList)
# a = myList[1:5]
# a = myList[::2]
# a = myList[::-1]
# print(a)
# print(len(myList))
# List1 = myList.copy()
# List1 = list(myList)
# List1 = myList[:]
# print(List1)

List2 = [1, 2, 3, 4]

List3 = [n*n for n in List2]
print(List3)

sexy = [0, 2, 4, 6, 8, ]
# myList.sort()
print("*"*50)
print(myList)

dhanoSquare = [m*m for m in sexy]
print(dhanoSquare)
print("*"*50)
print("*"*50)

# Sort() changes the original list
# Sorted(list, key)
var = [1, 2, 7, 9, 4, 5]
var1 = ["Amit", "Kumar", "Ani"]
var1.sort(key=len)
print(var1)
print("*"*50)
var.sort(reverse=True)
print(var)
print("*"*50)
variable = [1, 5, 3, 2, 4]
print(sorted(variable))
print(sorted(variable, reverse=True))
var2 = ["Amit", "Kumar", "Ani", "Amiiiii"]
print("*"*50)
print(sorted(var2, key=len))
print("*"*50)
print(variable)
print(sorted(variable, reverse=True))
print("*"*50)
vari = [1, 4, 3]
