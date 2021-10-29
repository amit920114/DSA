# Stack Implementation Usinf Linked List


class Node:
    def __init__(self, data) -> None:
        self.Data = data
        self.Next = None


class Stack:
    def __init__(self) -> None:
        self.__head = None
        self.count = 0

    def insert(self, val):
        newNode = Node(val)
        newNode.Next = self.__head
        self.__head = newNode
        self.count += 1

    def isEmpty(self):
        return self.count == 0

    def size(self):
        return self.count

    def top(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.__head.Data

    def remove(self):

        if self.isEmpty():
            return "Stack is Empty"
        data = self.__head.Data
        self.__head = self.__head.Next
        self.count -= 1
        return data

    def printStack(self):
        while self.__head:
            print(str(self.__head.Data) + "->", end="")
            self.__head = self.__head.Next
        print("None")
        return


s = Stack()
s.insert(1)
s.insert(2)
s.insert(3)
s.insert(4)
s.insert(5)
s.insert(6)
print(s.remove())
print(s.size())
print(s.top())
s.printStack()
print(s.isEmpty())
