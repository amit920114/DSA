# Dictionaries: Key, Value Pairs are known to be Dictionaries

intro = {"name": "Amit", "age": 22, 114920: "Kumar"}
# print(intro)
# print(type(intro))

amitIntro = intro.copy()
# print(amitIntro)

c = dict([("name", "Anil"), ("age", 32), (114920, "Gupta")])
# print(c)

g = dict.fromkeys(["name", "age", 35142], "Suar")
# print(g)
# print(intro.get("nam", 10101010))
# print(intro["name"])

# print(intro.items())
# print("name" in intro)

# Lecture 02 Frequency

s = "My name is Amit Kumar My friend name is Sujata ameer ameer ameer Amit Amit Amit"
words = s.split()
dic = {}
for k in words:
    if k in dic:
        dic[k] = dic[k] + 1
    else:
        dic[k] = 1
# print(dic)
for w in words:
    dic[w] = dic.get(w, 0) + 1


def countFreq(words, k):
    dic = {}
    for w in words:
        dic[w] = dic.get(w, 0) + 1
    for w in dic:
        if dic[w] == k:
            print(w)


print(dic)
countFreq(words, 4)
