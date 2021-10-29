from reverse import linkedList
from reverse import printLL


def reverse3(head):
    if head is None:
        return head
    if head.Next is None:
        return head
    smallOp = reverse3(head.Next)
    tail = head.Next
    tail.Next = head
    head.Next = None
    return smallOp


def reverse5(head):
    prev = None
    current = head
    while current:
        nxt = current.Next
        current.Next = prev
        prev = current
        current = nxt
    head = prev
    return head


head = linkedList()
printLL(head)
# op = reverse3(head)
op = reverse5(head)
printLL(op)
