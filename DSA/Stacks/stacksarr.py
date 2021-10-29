# Stack Using Array's


class Stack:
    def __init__(self):
        self.__data = []

    def push(self, item):
        self.__data.append(item)

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
            return
        return self.__data.pop()

    def top(self):
        if self.isEmpty():
            print("Hey stack is Empty !!")
            return
        return self.__data[len(self.__data) - 1]

    def size(self):
        return len(self.__data)

    def isEmpty(self):
        return self.__data == 0


s = Stack()
s.push(10)
s.push(30)
s.push(69)
s.push(64)
print(s.pop())
print(s.top())
print(s.isEmpty())
print(s.size())
