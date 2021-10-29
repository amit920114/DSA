# Queue Using Array's


class Queue:
    def __init__(self):
        self.__data = []
        self.__front = 0
        self.count = 0

    def enqueue(self, item):
        self.__data.append(item)
        self.count += 1
        # self.__front += 1

    def dequeue(self):
        if self.isEmpty():
            return print("Queue is Empty")
        pop = self.__data[self.__front]
        self.__front += 1
        self.count -= 1
        return pop

    def front(self):
        if self.isEmpty():
            return print("Queue is Empty")
        return self.__data[self.__front]

    def size(self):
        return self.count

    def isEmpty(self):
        return len(self.__data) == 0


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.front())
print(q.size())
print(q.isEmpty())
print("Before Dequeue")
print(q.dequeue())
print(q.dequeue())
print("After Dequeue")
print(q.front())
print(q.size())
print(q.isEmpty())
