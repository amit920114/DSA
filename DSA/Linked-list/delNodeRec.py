# Delete a Node Recursively at n-th Position
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


def delRecN(head, position):
    # prev = head
    if head is None:
        return None
    if position < 0:
        return head
    # prev = head
    if position == 0:
        current = head
        nxt = current.Next
        # # prev.Next = nxt
        return nxt

    smallHead = delRecN(head.Next, position - 1)
    # prev = head
    head.Next = smallHead
    return head


head = linkedList()
printLL(head)
# op = delRecN(head, 2)
op = delRecN(head, 0)
printLL(op)
