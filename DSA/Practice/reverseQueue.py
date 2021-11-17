# Reverse a Queue from a Particular Index:-

from queue import Queue


def reverse2(q, n):
    if q.empty() or n > q.qsize():
        return
    if n <= 0:
        return
    stack = []
    for i in range(n):
        stack.append(q.get())
    while len(stack) != 0:
        q.put(stack.pop())
    for k in range(q.qsize() - n):
        q.put(q.get())


def printQue(q):
    while not q.empty():
        print(q.get(), end=" ")


q = Queue()
q.put(10)
q.put(20)
q.put(30)
q.put(40)
q.put(50)
reverse2(q, 2)
printQue(q)
