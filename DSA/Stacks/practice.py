# Stacks Practice


class Stack:
    def __init__(self):
        self.__data = []

    def push(self, item):
        self.__data.append(item)

    def pop(self):

        if self.isEmpty():
            return print("Stack is Empty")
        return self.__data.pop()

    def top(self):
        if self.isEmpty():
            return print("Stack is Empty")
        return self.__data[len(self.__data) - 1]

    def size(self):
        return len(self.__data)

    def isEmpty(self):
        return self.__data == 0


s = Stack()
s.push(69)
s.push(64)
s.push(68)
s.push(99)
print(s.size())
print(s.top())
print(s.isEmpty())
print("---------")
print(s.pop())

print(s.top())
print(s.size())
print(s.isEmpty())
