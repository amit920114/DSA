# Linked List


class Node:
    def __init__(self, data) -> None:
        self.Data = data
        self.Next = None


def inputLL():
    inputList = [int(elem) for elem in input().split()]
    head = None
    tail = None
    for currentElem in inputList:
        if currentElem == -1:
            break
        newNode = Node(currentElem)
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


def countLL(head):
    if head is None:
        return 0
    return 1 + countLL(head.Next)


def appendToLast(head, n):
    count = countLL(head)
    prev = None
    curr = head
    skip = count - n
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


head = inputLL()
printLL(head)
# print(countLL(head))
nToLast = appendToLast(head, 3)
printLL(nToLast)
