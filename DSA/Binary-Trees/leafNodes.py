# Count number of Leaf Nodes:-
import queue


class BinaryTree:
    def __init__(self, data):
        self.Data = data
        self.left = None
        self.right = None


def treeInput():
    q = queue.Queue()
    print("Enter root:")
    rootData = int(input())
    if rootData == -1:
        return
    root = BinaryTree(rootData)
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        print("Enter left Child of ", currentNode.Data)
        leftChildData = int(input())
        leftChild = BinaryTree(leftChildData)
        if leftChildData != -1:
            currentNode.left = leftChild
            q.put(leftChild)

        print("Enter right Child of ", currentNode.Data)
        rightChildData = int(input())
        rightChild = BinaryTree(rightChildData)
        if rightChildData != -1:
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


def takeInput():
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTree(rootData)
    root.left = takeInput()
    root.right = takeInput()
    return root


def leafNodes(root):
    if root is None:
        return 0
    if root.left == None and root.right == None:
        return 1
    left = leafNodes(root.left)
    right = leafNodes(root.right)
    return left + right


root = treeInput()
printBT(root)
print(leafNodes(root))
