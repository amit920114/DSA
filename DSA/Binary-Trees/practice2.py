# Level-Wise Binary Tree:-
from levelwiseBT import takeLevelWiseInput
import queue


class BinaryTree:
    def __init__(self, data):
        self.Data = data
        self.left = None
        self.right = None


def takeInputLevelWise():
    q = queue.Queue()
    print("Enter root")
    rootData = int(input())
    if rootData == -1:
        return
    root = BinaryTree(rootData)
    q.put(root)
    while not (q.empty()):
        currentNode = q.get()
        leftChildData = int(input())
        if leftChildData != -1:
            print("Enter left child of", currentNode.Data)
            leftChild = BinaryTree(leftChildData)
            currentNode.left = leftChild
            q.put(leftChild)

        rightChildData = int(input())
        if rightChildData != 1:
            print("Enter right child of", currentNode.Data)
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


root = takeLevelWiseInput()
printBT(root)
