# Generators

def my_gen():
    yield 1
    yield 2
    yield 3


gen = my_gen()
# print(list(gen))
# print(gen)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

print(sum(gen))
print("*"*50)
print("while", "*"*50)


def gener(num):
    print("Starting")
    while num > 0:
        yield num
        num -= 1


cd = gener(5)
#
# val = next(cd)
# print(next(cd))
# print(val)
# print("*"*50)
print(sum(cd))
# print(next(cd))

print("*"*50)
print("less Memory")
print("*"*50)


def firstN(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums


b = firstN(5)
print(b)
print("*"*50)
print("Via Generators")


def frstN(n):
    num = 0
    while num < n:
        yield num
        num += 1


cc = frstN(10)
print(next(cc))
print(next(cc))
print(next(cc))
print(next(cc))
print(next(cc))

# Fibonacii series using generators
# 0 1 1 2 3 5 8 13
print("*"*50)
print("Fibonacciii")


def fibonacii(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a+b


ccc = fibonacii(5)
# print(sum(ccc))
for i in ccc:
    print(i)

# Generators expressions
print("*"*50)

print("Generators expressions")

vv = (o for o in range(10) if o % 2 == 0)
print(vv)
for k in vv:
    print(k)
print("With Lists")
ll = [h for h in range(10) if h % 2 == 0]
print(ll)
for l in ll:
    print(l)
