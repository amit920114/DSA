# Recursively insert at i-th position in a Singlly Linked List:-


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


def recInsN(head, item, position):
    if position < 0:
        return head
    if head is None:
        return None
    if position == 0:
        current = head
        newNode = Node(item)
        head = newNode
        newNode.Next = current
    smallHead = recInsN(head.Next, item, position - 1)
    head.Next = smallHead
    return head


head = linkedList()
printLL(head)
# op = recInsN(head, 9, 2)
op = recInsN(head, 9, 0)
printLL(op)
