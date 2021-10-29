# Reverse A Queue:


class ReverseQueue:
    def __init__(self):
        self.__s1 = []
        self.__s2 = []

    def enqueue(self, data):
        self.__s1.append(data)
        while len(self.__s1) != 0:
            self.__s2.append(self.__s1.pop())
        return

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
        return self.__s2.pop()

    def front(self):
        if self.isEmpty():
            print("Queue is Empty")
        return self.__s2[-1]

    def size(self):
        return len(self.__s2)

    def isEmpty(self):
        return self.size() == 0


q = ReverseQueue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
# print("10->20->30->40")
print(q.front())
print(q.dequeue())
print(q.front())
