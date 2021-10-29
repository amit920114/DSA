# Delete a Node


class Node:
    def __init__(self, data):
        self.Data = data
        self.Next = None


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


def lengthLL(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.Next
    return count


def deleteNode(head, position):
    if position < 0 or position >= lengthLL(head):
        return head
    nxt = None
    prev = None
    count = 0
    current = head

    while count < position:
        count += 1
        prev = current
        current = current.Next
        nxt = current.Next
    if prev is not None:
        prev.Next = nxt
    else:
        head = current.Next
    current.Next = nxt
    return head


head = linkedList()
printLL(head)
op = deleteNode(head, 5)
# op = deleteNode(head, 0)
printLL(op)
