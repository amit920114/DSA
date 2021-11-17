# Binary Search Tree:-
import queue


class BinaryTree:
    def __init__(self, data):
        self.Data = data
        self.right = None
        self.left = None


def takeInput():
    q = queue.Queue()
    print("Enter root:")
    rootData = int(input())
    if rootData == -1:
        return
    root = BinaryTree(rootData)
    q.put(root)
    while not (q.empty()):
        currentNode = q.get()
        print("Enter left Child of", currentNode.Data)
        leftChildData = int(input())
        if leftChildData != -1:
            leftChild = BinaryTree(leftChildData)
            currentNode.left = leftChild
            q.put(leftChild)
        print("Enter right Child of", currentNode.Data)
        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = BinaryTree(rightChildData)
            currentNode.right = rightChild
            q.put(rightChild)

    return root


def printBT(root):
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


def bst(root, x):
    if root is None:
        return False
    if root.Data == x:
        return True
    if root.Data > x:
        return bst(root.left, x)
    else:
        return bst(root.right, x)


def bstV2(root, x):
    if root is None:
        return
    if root.Data == x:
        return root
    if root.Data > x:
        return bstV2(root.left, x)
    else:
        return bstV2(root.right, x)


root = takeInput()
printBT(root)
print()
# print(bst(root, 6))
bsT = bstV2(root, 6)
printBT(bsT)
