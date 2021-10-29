# Predict The Output


# from insNode import linkedList
# from lect5 import takeInput


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# def printLL(head):
#     while head is not None:
#         print(head.data, end=" ")
#         head = head.next
#         # print(head)


# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node4 = Node(40)
# node2.next = node3
# node3.next = node4
# printLL(node2)

# Insert At N-th position in a Linked-List


# from typing import Counter


# class Node:
#     def __init__(self, data):
#         self.Data = data
#         self.Next = None


# def linkedList():
#     inputList = [int(elem) for elem in input().split()]
#     head = None
#     tail = None
#     for currentData in inputList:
#         if currentData == -1:
#             break
#         newNode = Node(currentData)
#         if head is None:
#             head = newNode
#             tail = newNode
#         else:
#             tail.Next = newNode
#             tail = newNode

#     return head


# def printLL(head):
#     while head:
#         print(str(head.Data) + "->", end="")
#         head = head.Next
#     print("None")
#     return


# def lengthLL(head):
#     count = 0
#     current = head
#     while current:
#         count += 1
#         current = current.Next
#     return count


# def insertN(head, item, position):
#     if position < 0 or position > lengthLL(head):
#         return head
#     count = 0
#     prev = None
#     current = head
#     while count < position:
#         count += 1
#         prev = current
#         current = current.Next
#     newNode = Node(item)
#     if prev is not None:
#         prev.Next = newNode
#     else:
#         head = newNode
#     newNode.Next = current
#     return head


# head = linkedList()
# printLL(head)
# # lengthLL(head)
# # op = insertN(head, 9, 2)
# # op = insertN(head, 9, 0)
# op = insertN(head, 9, 5)
# printLL(op)
op = 5 // 2
print(op)
