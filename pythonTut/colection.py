# Collections in Python is like containers these are Counter, namedtuple, orderDict,defaultdict,deque
# COUNTER:- Counter is a synclass of dictionaries used to count hasable values

from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import namedtuple
from collections import Counter
var = "AAAAABBBBBBCCCDD"
myCounter = Counter(var)
print(myCounter)
print("*"*50)
print(myCounter.items())
print(myCounter.values())
print(myCounter.keys())
print("*"*50)

print(myCounter.most_common(1)[0])
print("*"*50)

print(list(myCounter.elements()))
print("*"*50)
print("*"*50)

# namedTuple

Laila = namedtuple("Laila", "name,sex")

values = Laila("SavitaBhabhi", "Rand")
print(values)
print("*"*50)
print("*"*50)

Dhano = namedtuple("Dhano", "Age,City")
Description = Dhano("27", "New Delhi")
print(Description)
print("*"*50)
print("*"*50)

Darling = namedtuple("Darling", "Name, age")
des = Darling("Shilla", "32")
print(Darling)

Neha = namedtuple("Neha", "Age, Sex")
print("*"*50)
print("*"*50)

des1 = Neha("42", "Female")
print(des1)
print(des1.Age, des1.Sex)
print("*"*50)
print("*"*50)

# OrderedDict same as dictonaries
order_dic = OrderedDict()
order_dic["a"] = 5
order_dic["b"] = 6
order_dic["c"] = 7
order_dic["d"] = 8
order_dic["e"] = 9
order_dic["f"] = 10

print(order_dic)
print("*"*50)
print("*"*50)

# DefaultDIC
d = defaultdict(int)
d["a"] = 1
d["b"] = 2
d["c"] = 3
d["d"] = 4
d["e"] = "Namit"
print(d["g"])
print("*"*50)
print("*"*50)

# DEQUE in collections
dic = deque()
dic.append(1)
dic.appendleft(2)
dic.pop()
dic.extendleft([1, 0])
dic.extend([3, 4, 5])
print("*"*50)
print("*"*50)

# dic.clear()
dic.rotate(-1)

print(dic)
