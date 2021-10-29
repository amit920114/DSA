# Palindrome in Linked-List


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


def traverse(head, len):
    if head is None:
        return None
    current = head
    i = 0
    while i <= len:
        i += 1
        current.Next = None
        current = current.Next
        return current
    return head


def palindrome(head):
    if head is None:
        return None
    current = head
    # if current.Next is None:
    #     return False
    current = current.Next
    if head.Data == current.Data:
        return print(True)
    else:
        print(False)

    return palindrome(head.Next)


head = linkedList()
printLL(head)
op = traverse(head, 3)
printLL(op)
