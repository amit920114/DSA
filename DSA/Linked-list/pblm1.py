# print ith indexed value
class Node:
    def __init__(self, data):
        self.Data = data
        self.Next = None


def LinkedList():
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


def printLL(head, index):
    count = 0
    current = head
    while current:
        # while head is not None:
        if count == index:
            return print(current.Data)
        count += 1
        current = current.Next
    #     print(str(head.Data) + "->", end="")
    #     head = head.Next
    # print("None")
    # print("Amit")
    return


head = LinkedList()
printLL(head, 2)
# printLL(head)
