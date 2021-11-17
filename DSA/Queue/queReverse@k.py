# Reverse Queue from k'th element
from queue import Queue


def reverseQueue(k, q):
    if q.empty() == True or k > q.qsize():
        return
    if k <= 0:
        return
    stack = []
    for i in range(k):
        # stack.append(q.queue[0])
        stack.append(q.get())
        # q.get()
    while len(stack) != 0:
        # q.put(stack[-1])
        q.put(stack.pop())
        # stack.pop()
    for i in range(q.qsize() - k):
        # q.put(q.queue[0])
        q.put(q.get())
        # q.get()


def PrintQ(q):
    while not q.empty():
        print(q.queue[0], end=" ")
        q.get()


q = Queue()
q.put(10)
q.put(20)
q.put(30)
q.put(40)
q.put(50)
reverseQueue(2, q)
PrintQ(q)
