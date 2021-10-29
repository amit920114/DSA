# Find the Path of Node in a Binary Tree:-
import queue


class BInaryTree:
    def __init__(self, data):
        self.Data = data
        self.left = None
        self.right = None


def takeInput():
    q = queue.Queue()
    print("Enter root:")
    rootData = int(input())
    if rootData == -1:
        return
    root = BInaryTree(rootData)
    q.put(root)
    while not (q.empty()):
        currentNode = q.get()
        print("Enter left Child of", currentNode.Data)
        leftChildData = int(input())
        if leftChildData != -1:
            leftChild = BInaryTree(leftChildData)
            currentNode.left = leftChild
            q.put(currentNode.left)
        print("Enter right Child of", currentNode.Data)
        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = BInaryTree(rightChildData)
            currentNode.right = rightChild
            q.put(currentNode.right)
    return root


def prinBt(root):
    q = queue.Queue()
    if root is None:
        return
    q.put(root)
    while not (q.empty()):
        currentNode = q.get()
        print(currentNode.Data, end=" ")
        if currentNode.left != None:
            q.put(currentNode.left)
        if currentNode.right != None:
            q.put(currentNode.right)


# ----------- Self.tried--------------- #

# data = []


# def path(root, x):
#     if root is None:
#         return
#     if root.left is None or root.right is None:
#         return data
#     if root.left.Data == x:
#         data.append(root.left.Data)
#         data.append(root.Data)
#     elif root.right.Data == x:
#         data.append(root.right.Data)
#         data.append(root.Data)
#     path(root.left, x)
#     path(root.right, x)
#     return data

# ----------- Self.tried--------------- #


def path(root, x):
    if root is None:
        return
    if root.Data == x:
        data = []
        data.append(root.Data)
        return data
    leftOp = path(root.left, x)
    if leftOp != None:
        leftOp.append(root.Data)
        return leftOp
    rightOp = path(root.right, x)
    if rightOp != None:
        rightOp.append(root.Data)
        return rightOp


root = takeInput()
prinBt(root)
print("")
print(path(root, 69))
