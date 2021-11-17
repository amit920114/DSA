# Binary Tree Implementation:-
import queue


class BinaryTree:
    def __init__(self, data) -> None:
        self.Data = data
        self.right = None
        self.left = None


def btInput():
    q = queue.Queue()
    print("Enter root")
    rootData = int(input())
    if rootData == -1:
        return
    root = BinaryTree(rootData)
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        print("Enter left child of", currentNode.Data)
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


def printBt(root):
    if root is None:
        return
    print(root.Data, end=":")
    if root.left != None:
        print("L", root.left.Data, end=",")
    if root.right != None:
        print("R", root.right.Data, end="")
    print()
    printBt(root.left)
    printBt(root.right)


def printLvl(root):
    q = queue.Queue()
    if root is None:
        return
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        print(currentNode.Data, end=" ")
        if currentNode.left != None:
            q.put(currentNode.left)
        if currentNode.right != None:
            q.put(currentNode.right)


root = btInput()
printBt(root)
printLvl(root)
