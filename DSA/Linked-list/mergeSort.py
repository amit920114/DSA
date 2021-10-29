# Merge Sort


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


def midLL(head):
    slow = head
    fast = head
    while fast.Next and fast.Next.Next:
        slow = slow.Next
        fast = fast.Next.Next
    return slow


def mergeTwoSortedLL(head1, head2):
    finalHead = None
    finalTail = None
    if head1.Data < head2.Data:
        finalHead = head1
        finalTail = head1
        head1 = head1.Next
    else:
        finalHead = head2
        finalTail = head2
        head2 = head2.Next
    while head1 and head2:
        if head1.Data < head2.Data:
            finalTail.Next = head1
            finalTail = finalTail.Next
            head1 = head1.Next
        else:
            finalTail.Next = head2
            finalTail = finalTail.Next
            head2 = head2.Next
    if head1:
        finalTail.Next = head1
    else:
        finalTail.Next = head2
    return finalHead


def mergeSort(head):
    if head.Next is None:
        return head
    mid = midLL(head)
    nextOfMid = mid.Next
    mid.Next = None
    left = mergeSort(head)
    right = mergeSort(nextOfMid)
    return mergeTwoSortedLL(left, right)


def printLL(head):
    while head:
        print(str(head.Data) + "->", end="")
        head = head.Next
    print("None")
    return


# head1 = linkedList()
# head2 = linkedList()
# printLL(head1)
# printLL(head2)
# op = mergeTwoSortedLL(head1, head2)
# printLL(op)

head = linkedList()
printLL(head)
# midLL(head)
op = mergeSort(head)
printLL(op)
