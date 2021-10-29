# Level-Wise Binary Tree:-
import queue


class BinaryTree:
    def __init__(self, data):
        self.Data = data
        self.left = None
        self.right = None


def takeLevelWiseInput():
    q = queue.Queue()
    print("Enter root")
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTree(rootData)
    q.put(root)
    while not (q.empty()):
        currentNode = q.get()
        print("Enter left child of ", currentNode.Data)
        leftChildData = int(input())
        if leftChildData != -1:
            leftChild = BinaryTree(leftChildData)
            currentNode.left = leftChild
            q.put(leftChild)

        print("Enter right child of", currentNode.Data)
        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = BinaryTree(rightChildData)
            currentNode.right = rightChild
            q.put(rightChild)
    return root


def printBT(root):
    if root is None:
        return
    print(root.Data, end=":")
    if root.left != None:
        print("L", root.left.Data, end=",")
    if root.right != None:
        print("R", root.right.Data, end="")
    print()
    printBT(root.left)
    printBT(root.right)


def printBTV2(root):
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


root = takeLevelWiseInput()
printBT(root)
printBTV2(root)
