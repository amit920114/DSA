# Practice
# Stacks using Linked-List


class Node:
    def __init__(self, data) -> None:
        self.Data = data
        self.Next = None


class Stack:
    def __init__(self):
        self.__head = None
        self.__count = 0

    def push(self, element):
        newNode = Node(element)
        newNode.Next = self.__head
        self.__head = newNode
        self.__count += 1

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
            return
        data = self.__head.Data
        self.__head = self.__head.Next
        self.__count -= 1
        return data

    def top(self):

        if self.isEmpty():
            print("Stack is Empty")
            return
        return self.__head.Data

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.__count == 0


s = Stack()
s.push(10)
s.push(20)
print(s.pop())
