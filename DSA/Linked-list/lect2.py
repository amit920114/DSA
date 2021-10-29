# Linked List:- Unlike Lists it has elements as well as next/Reference to next node


class Node:
    def __init__(self, data):
        self.Data = data
        self.Next = None


a = Node(5)
print(a)
print(a.Data)
b = Node(7)
a.Next = b
print(a.Next)
print(a.Next.Data)
# print(b.Next)
c = Node(9)
b.Next = c
print(b.Next.Data)
print(a.Next.Data)
print(c.Data)
print(c.Next)
