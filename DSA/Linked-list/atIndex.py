# Find nNode in Linked List


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


# <--------------------IgNoreee------------------------>

# def apendToLast(head,position):
#     current = head
#     count = 0
#     fixedHead = head
#     while current:
#         if count == position:
#             head = current
#             while head:
#                 head.Next = current.Next
#             if fixedHead == current:
#                 break
#             if head is None:
#                 head.Next = fixedHead
# <---------------------------IgNoreee------------------>


def printLL(head):
    while head:
        print(str(head.Data) + "->", end="")

        head = head.Next
    print("None")
    return


def findNode(head, item):

    current = head
    count = 0
    newNode = Node(item)
    while current:
        if current.Data == newNode.Data:
            return count
        count += 1
        current = current.Next
    if current is None:
        return -1
    return count


head = linkedList()
printLL(head)
# op = findNode(head, 1) --> Worked
op = findNode(head, 9)

print(op)
