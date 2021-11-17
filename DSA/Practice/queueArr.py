# Queue Using Array:-


class Queue:
    def __init__(self) -> None:
        self.__data = []
        self.__count = 0
        self.__front = 0

    def insert(self, val):
        self.__data.append(val)
        self.__count += 1

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return self.__count

    def remove(self):
        if self.isEmpty():
            return "Queue is Empty"
        data = self.__data[self.__front]
        self.__front += 1
        self.__count -= 1
        return data

    def front(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.__data[self.__front]


q = Queue()

print(q.isEmpty())
print(q.front())
print(q.remove())
print(q.size())
q.insert(1)
q.insert(2)
q.insert(3)
q.insert(4)
q.insert(5)
print(q.size())
print(q.isEmpty())
print(q.front())
print(q.remove())
print(q.remove())
