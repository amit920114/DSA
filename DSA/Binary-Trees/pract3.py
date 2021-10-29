# 3 days after working with office and computer repair things, Hope i Will Complete DSA ASAP in Month of October as Decided.
# Jai Shiv Shambhu, Jai Mata Di, Jai Bajrang Bali
import queue


class BinaryTree:
    def __init__(self, data):
        self.Data = data
        self.left = None
        self.right = None


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


def takeInput():
    rootData = int(input())
    if rootData == -1:
        return
    root = BinaryTree(rootData)
    root.left = takeInput()
    root.right = takeInput()
    return root


def takeInputLevelwise():
    q = queue.Queue()
    print("Enter root:")
    rootData = int(input())
    if rootData == -1:
        return
    root = BinaryTree(rootData)
    q.put(root)
    while not (q.empty()):
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


def printLevelWise(root):
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


def preOrder(root):
    if root is None:
        return
    data = []
    data.append(root)
    while len(data) > 0:
        node = data.pop()
        print(node.Data, end=" ")
        if node.right != None:
            data.append(node.right)
        if node.left != None:
            data.append(node.left)


root = takeInputLevelwise()
printLevelWise(root)
print()
# printBT(root)
preOrder(root)
