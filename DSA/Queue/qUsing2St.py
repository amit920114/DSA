# Queue Using Two Stacks


class QueueUsingTwoStacks:
    def __init__(self):
        self.__s1 = []
        self.__s2 = []

    def enqueue(self, data):
        while len(self.__s1) != 0:
            self.__s2.append(self.__s1.pop())
        self.__s1.append(data)
        while len(self.__s2) != 0:
            self.__s1.append(self.__s2.pop())
        return

    def dequeue(self):
        if len(self.__s1) == 0:
            return print("Queue is Empty")
        return self.__s1.pop()

    def front(self):
        return self.__s1[-1]

    def size(self):
        return len(self.__s1)

    def isEmpty(self):
        return self.size() == 0


q = QueueUsingTwoStacks()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
print(q.front())
print(q.size())
print(q.isEmpty())
print("1Dequeue element:-", q.dequeue())
print("2Dequeue element:-", q.dequeue())
print(q.front())
print(q.size())
print(q.isEmpty())
print("3Dequeue element:-", q.dequeue())
print(q.front())
print("4Dequeue element:-", q.dequeue())
# print(q.front())
print(q.size())
print(q.isEmpty())
