# Tree Travarsal:-
# 1. Pre Order
# 2. Post Order
# 3. In-line Order
# 4. Level-wise order

# 1. PRE ORDER
import queue


class BinaryTree:
    def __init__(self, data):
        self.Data = data
        self.left = None
        self.right = None


def printBTreePre(root):
    if root is None:
        return None
    print(root.Data, end=":")
    if root.left != None:
        print("L", root.left.Data, end=",")
    if root.right != None:
        print("R", root.right.Data, end="")
    print()
    printBTreePre(root.left)
    printBTreePre(root.right)


def printPreOrder(root):
    if root is None:
        return
    print(root.Data)
    printPreOrder(root.left)
    printPreOrder(root.right)


def printBTreePost(root):
    if root is None:
        return None
    printBTreePost(root.left)
    printBTreePost(root.right)
    print(root.Data)


def takeInput():
    rootData = int(input())
    if rootData == -1:
        return
    root = BinaryTree(rootData)
    root.left = takeInput()
    root.right = takeInput()
    return root


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


def printInline(root):
    if root is None:
        return
    printInline(root.left)
    print(root.Data)
    printInline(root.right)


root = treeInput()
printBTreePre(root)
print()
printBTreePost(root)
print()

# printPreOrder(root)
printInline(root)
