# Practice Linked-List


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


def countLL(head):
    count = 0
    while head:
        count += 1
        head = head.Next
    return count


def countLRe(head, count=0):
    if head is None:
        return 0
    return countLRe(head.Next, count + 1) + 1


head = linkedList()
printLL(head)
# print(countLL(head))
print(countLRe(head))
