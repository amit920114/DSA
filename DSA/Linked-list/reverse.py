# Pratice will start at Night
# Reverse a Linked List


from reverseLink import reverseLL2


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


def reverseLL(head):
    current = head
    if current is None:
        return current
    if current.Next is None:
        head = current
        return head
    node = reverseLL(head.Next)
    current.Next.Next = current
    current.Next = None
    return node


def reverse2(head):
    prev = None
    nxt = None
    current = head
    while current:
        nxt = current.Next
        current.Next = prev
        prev = current
        current = nxt
    head = prev
    return head


def printLL(head):
    while head:
        print(str(head.Data) + "->", end="")
        head = head.Next
    print("None")
    return


head = linkedList()
printLL(head)
op = reverseLL2(head)
printLL(op)
