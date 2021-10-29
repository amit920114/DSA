# Length Of Linked List


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


def loLL(head):

    count = 0
    current = head
    while current:
        count += 1
        current = current.Next

    return print(count)
    # print(head.Data)


head = LinkedList()
loLL(head)
