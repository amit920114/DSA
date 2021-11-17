# Queue Using Linked-List


class Node:
    def __init__(self, data) -> None:
        self.Data = data
        self.Next = None


class Queue:
    def __init__(self) -> None:
        self.__head = None
        self.__tail = None
        self.__count = 0

    def insert(self, val):
        newNode = Node(val)
        if self.__head is None:
            self.__head = newNode
        else:
            self.__tail.Next = newNode
        self.__tail = newNode
        self.__count += 1

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.size() == 0

    def remove(self):
        if self.isEmpty():
            return "Queue is Empty"
        data = self.__head.Data
        self.__count -= 1
        self.__head = self.__head.Next
        return data

    def top(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.__head.Data


q = Queue()


# print(q.isEmpty())
# print(q.size())
# print(q.top())
# print(q.remove())
q.insert(1)
q.insert(2)
q.insert(3)
q.insert(4)
q.insert(5)
print(q.top())
print(q.remove())
print(q.size())
print(q.top())
