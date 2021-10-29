# Find The Mid-Pont off Th linked List


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
    current = head
    count = 0
    while current:
        count += 1
        current = current.Next
    return print(count)


def midLL(head):
    slow = head
    fast = head
    while fast.Next and fast.Next.Next:
        slow = slow.Next
        fast = fast.Next.Next
    return slow.Data


head = linkedList()
printLL(head)
lengthLL(head)
op = midLL(head)
print(op)
