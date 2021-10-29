# Reverse a Stack


def reverse(s1, s2):
    # s1 = [input]
    # s2 = []
    if len(s1) == 1:
        return s1
    while len(s1) != 1:
        elem = s1.pop()
        s2.append(elem)
    x = s1.pop()
    while len(s2) != 0:
        elem = s2.pop()
        s1.append(elem)
    reverse(s1, s2)
    s1.append(x)
    return s1


s1 = [1, 2, 3]
s2 = []
print(reverse(s1, s2))
