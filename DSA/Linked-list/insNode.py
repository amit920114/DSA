# Insert Node at specific Position


# from loll import loLL


class Node:
    def __init__(self, data):
        self.Data = data
        self.Next = None


def linkedList():
    inputList = [int(elem) for elem in input().split()]
    head = None
    tail = None
    for currentElement in inputList:
        if currentElement == -1:
            break
        newNode = Node(currentElement)
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

    return count


def insertN(head, item, position):

    if position < 0 or position > loLL(head):
        return head

    count = 0
    prev = None
    current = head
    while count < position:
        prev = current
        current = current.Next
        count += 1
    newNode = Node(item)
    if prev is not None:
        prev.Next = newNode
    else:
        head = newNode
    newNode.Next = current
    # newCurrent = current.Next

    # while count < position:
    #     if count == position - 1:
    #         current.Next = item
    #         item.Next = newCurrent
    #     print(str(current.Data) + "->", end="")
    #     count += 1
    return head


def printLL(head):
    # while head is not None:
    while head:
        print(str(head.Data) + "->", end="")
        head = head.Next
    print("None")
    return


head = linkedList()
printLL(head)

head = insertN(head, 9, 1)
printLL(head)
