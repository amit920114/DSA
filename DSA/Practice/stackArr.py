# implementation OF Stacks using Array


class Stack:
    def __init__(self) -> None:
        self.__data = []

    def push(self, val):
        self.__data.append(val)

    def size(self):
        return len(self.__data)

    def isEmpty(self):
        return self.size == 0

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.__data.pop()

    def top(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.__data[-1]

    def printStack(self):
        return self.__data


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.pop()
print(s.printStack())
print(s.size())
print(s.isEmpty())
print(s.top())
