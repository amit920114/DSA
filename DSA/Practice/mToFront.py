# Append last m elements to front of Linked List:-


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


def mToLast(head, m):
    if head is None:
        return
    prev = None
    curr = head
    skip = countLL(head) - m
    while skip > 0:
        prev = curr
        curr = curr.Next
        skip -= 1
    prev.Next = None
    tempHead = head
    head = curr
    while curr.Next:
        curr = curr.Next
    curr.Next = tempHead
    return head


def atIndex(head, n):
    if head is None:
        return
    i = 0
    curr = head
    newNode = Node(n)
    while curr:
        if curr.Data == newNode.Data:
            return i
        i += 1
        curr = curr.Next
    if curr is None:
        return -1
    return i


head = inputLL()
printLL(head)
# print(countLL(head))
# head2 = mToLast(head, 3)
# printLL(head2)
print(atIndex(head, 5))
