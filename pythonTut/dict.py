# Dictonaries are the collections of unordered data types, and are mutable having key value pairs:-

# myDict = {
#     "name": "Amit",
#     "age": 27,
#     "city": "Delhi"
# }
# print(myDict)
print("*"*50)
print("*"*50)
# myDict = dict(name="Amit", age=28, city="UP")
myDict2 = dict(name="Ajay", age=26, city="Gujrat")
print(myDict2)
print(myDict2["city"])
print(myDict2["name"])

newVal = myDict2["email"] = "mygmail!@.com"
print("*"*40)
print("*"*40)
print(myDict2)

print("*"*40)
print("*"*40)

# To delete

del myDict2["email"]


# print(myDict2.pop("name"))
toDel = myDict2.pop("name")
myDict2["name"] = "Shanti"
myDict2.popitem()
myDict2["name"] = "Shakuntla"
# To check
if "lastname" in myDict2:
    print(myDict2["name"])
else:
    print("NoOne")

try:
    print(myDict2["age"])
except:
    print("NO BOdy")
print(myDict2)
# Looping

for d, z in myDict2.items():
    print(d, z)
print("*"*40)
print("*"*40)

for s in myDict2.keys():
    print(s)
print("*"*40)
print("*"*40)
for f in myDict2.values():
    print(f)
print("*"*40)
print("*"*40)
myDict3 = myDict2.copy()
print(myDict3)
print("*"*40)
print("*"*40)
myDict4 = dict(myDict3)
print(myDict4)

myDict5 = dict(name="Sonali", age=36, sex="female")
myDict4.update(myDict5)
print("*"*40)
print("*"*40)
print("*"*40)
print(myDict4)

myDict6 = {
    "name": "Suhil"
}
print(myDict6["name"])

# Tuples can be added in dictonaries

myTuple = (4, 5)
myDict7 = {
    myTuple: 9
}
print(myDict7)

print("#"*50)


def funcName(list):
    for k in list:
        print(k)


list = [1, 2, 3, 4, 5]
print(funcName(list))
