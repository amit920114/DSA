# Getting Inputs from The User
# Linked List


class Node:
    def __init__(self, data):
        self.Data = data
        self.Next = None


# 1 2 3 4 5 -1


def takeInput():
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
            # current = head
            # while current.Next is not None:
            #     current = current.Next
            # current.Next = newNode
            tail.Next = newNode
            tail = newNode
    return head


def printLL(head):
    # while head is not None:
    while head:
        print(str(head.Data) + "->", end="")
        head = head.Next  # head.next yha ho rha h bhai
    print("None")
    return


head = takeInput()
printLL(head)
