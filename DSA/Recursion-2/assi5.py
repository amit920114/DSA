# String to Number

def stoN(str, l):
    if l == 1:
        return ord(str[0]) - ord("0")
    lastVal = ord(str[l-1]) - ord("0")
    k = stoN(str, l-1)
    op = k*10 + lastVal
    return op


print(type(stoN("9717782916", 10)))
# print(type(p))
k = 12212
# print(type(k))
