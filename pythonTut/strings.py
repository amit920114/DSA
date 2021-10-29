# Strings are immutable , ordered amd used for text representations
myString = "My name is Amit Kumar"
# Slicing
myString[::1]

print("*"*50)
print("*"*50)
print(myString)

print("*"*50)
print("*"*50)
print(myString[::-1])
print(myString[::-2])
print("*"*50)
print("*"*50)
# Concetinations
var1 = "My name is "
var2 = "AMIT KUMAR"
print(var1+var2)
# Iterations

for g in var2:
    print(g)
if "AMIT  " in var2:
    print(True)
else:
    print(False)
print("*"*50)
print("*"*50)
var3 = "    AMIT    kumar"
print(var3)
print(var3.strip())
print(var3.upper())
print(var3.lower())
print(var3.startswith('    AMIT'))
print(var3.endswith('    AMIT'))
print(var3.find('AMIT'))
print(var3.count('A'))
print(var3.replace('A', "Z"))
# print("*"*50)
print("*"*50)
print("*"*50)
newString = "My name is Amit Kumar"
print(newString.split(" "))
print("*"*50)
print("*"*50)
myList = ["My", "Name", "Is", "Amit"]
print(myList)
new_string = " ".join(myList)
print(new_string)
print("*"*50)
print("*"*50)
var5 = ""
for i in myList:
    var5 += i
    print(var5)
# Formatting in Strings
str = "Amit "
str2 = "Kumar"
#
print("*"*50)
print("*"*50)
new_str = f"My first name is {str *2} and last name is {str2}"
print(new_str)
