# Reverse a Singly Linked-list


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


# <-----------------------Iterative Method O(n) time complexity Method----------------->
def reverseLL(head):
    current = head
    prev = None
    nxt = None
    while current:
        nxt = current.Next
        current.Next = prev
        prev = current
        current = nxt
    head = prev
    return head


# def tried(head):
#     current = head
#     prev = None
#     nxt = None
#     while current:
#         nxt = current.Next
#         current.Next = prev
#         prev = current
#         current = nxt
#     head = prev
#     return head

# <-----------------------Recurcive Method  O(n) time complexity----------------->


def reverseLL2(head):
    current = head
    if current is None:
        return None
    if current.Next is None:
        head = current
        return head
    node = reverseLL2(head.Next)
    current.Next.Next = current
    current.Next = None
    return node


head = linkedList()
printLL(head)
# lengthLL(head)
# op = reverseLL(head)
op = reverseLL2(head)
printLL(op)
