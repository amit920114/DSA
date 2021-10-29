# Find Node in Linked-List Recursively


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


def findNode(head, item, count=0):
    if head is None:
        return -1
    # count = 0
    newNode = Node(item)
    if head.Data == newNode.Data:
        return count
    # count += 1
    # head = head.Next

    # count += 1
    # head = head.Next
    # return findNode(head.Next, item)
    return findNode(head.Next, item, count + 1)


head = linkedList()
printLL(head)
op = findNode(head, 3)
print(op)
