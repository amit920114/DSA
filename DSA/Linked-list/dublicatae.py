# Remove Dublicacy in Linked-list


from typing import NewType


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


# -----------------Iterarive Method------------------->
def dublicate(head):
    current = head

    while current:
        nextNode = current.Next
        if nextNode is None or current.Data != nextNode.Data:
            current = nextNode
        else:
            current.Next = nextNode.Next

    return head


# -----------------End------------------->

# --------------------Recursive Method-------------------->

# Behnchooooooo khud se hi ho gya hahahahahahahahahahahahaha___________
def dublicate2(head):
    current = head
    nextNode = current.Next
    if current is None:
        return head
    if current.Data == nextNode.Data:
        current.Next = nextNode.Next
    current = current.Next
    dublicate(head.Next)
    return head


head = linkedList()
printLL(head)
# op = dublicate(head) #---Iterative
op = dublicate2(head)  # -------Recursive
printLL(op)
