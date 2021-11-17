# Queue using Linked-List


class Node:
    def __init__(self, data):
        self.Data = data
        self.Next = None


class Queue:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def enqueue(self, data):
        newNode = Node(data)
        if self.__head is None:
            self.__head = newNode
        else:
            self.__tail.Next = newNode
        self.__tail = newNode
        self.__count += 1

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        pop = self.__head.Data
        self.__head = self.__head.Next

        self.__count -= 1
        return pop

    def front(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        return self.__head.Data

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.__count == 0


def linkedList():
    inputList = [int(elem) for elem in input().split()]
    head = None
    tail = None
    for currentData in inputList:
        if currentData == -1:
            break
        newNode = Node(currentData)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.Next = newNode
            tail = newNode
    return head


def printLL(head):
    while head:
        print(str(head.Data) + "->", end="")
        head = head.Next
    print("None")
    return


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
print(q.front())
print(q.size())
print(q.isEmpty())
print("Before Dequeue")
print("Dequeue element:-", q.dequeue())
print("After Dequeue")
print(q.front())
print(q.size())
print(q.isEmpty())
