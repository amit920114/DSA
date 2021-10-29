# Append to Last


class Node:
    def __init__(self, data):
        self.Data = data
        self.Next = None


def linkedList():
    inputList = [int(elem) for elem in input().split()]
    head = None
    tail = None
    for currenrtData in inputList:
        if currenrtData == -1:
            break
        newNode = Node(currenrtData)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.Next = newNode
            tail = newNode
    return head


def countLL(head):
    if head is None:
        return 0
    return 1 + countLL(head.Next)


def appendToLast(head, m):
    count = countLL(head)
    prev = None
    curr = head
    skip = count - m
    while skip > 0:
        prev = curr
        curr = curr.Next
        skip -= 1
    prev.Next = None
    tempHead = head
    head = curr
    while curr.Next != None:
        curr = curr.Next
    curr.Next = tempHead
    return head


def printLL(head):
    while head:
        print(str(head.Data) + "->", end="")
        head = head.Next
    print("None")
    return


head = linkedList()
printLL(head)
# print(countLL(head))
nToLast = appendToLast(head, 3)
printLL(nToLast)
