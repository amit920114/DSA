# Trees:
import queue


class TreeNode:
    def __init__(self, data) -> None:
        self.Data = data
        self.left = None
        self.right = None


def treeInput():
    q = queue.Queue()
    print("Enter root:")
    rootData = int(input())
    if rootData == -1:
        return
    root = TreeNode(rootData)
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        print("Enter left Child of ", currentNode.Data)
        leftChildData = int(input())
        leftChild = TreeNode(leftChildData)
        if leftChildData != -1:
            currentNode.left = leftChild
            q.put(leftChild)

        print("Enter right Child of ", currentNode.Data)
        rightChildData = int(input())
        rightChild = TreeNode(rightChildData)
        if rightChildData != -1:
            currentNode.right = rightChild
            q.put(rightChild)
    return root


def printTree(root):
    if root is None:
        return
    print(root.Data, end=":")
    if root.left != None:
        print("L", root.left.Data, end=",")
    if root.right != None:
        print("R", root.right.Data, end="")
    print()
    printTree(root.left)
    printTree(root.right)


def printLvlWise(root):
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


def countNodes(root):
    if root is None:
        return 0
    left = countNodes(root.left)
    right = countNodes(root.right)
    return 1 + left + right


def sumNodes(root):
    if root is None:
        return 0
    left = sumNodes(root.left)
    right = sumNodes(root.right)
    return root.Data + left + right


def postOrder(root):
    if root is None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.Data)


def inOrder(root):
    if root is None:
        return
    inOrder(root.left)
    print(root.Data)
    inOrder(root.right)


def maxNode(root):
    if root is None:
        return -1
    left = maxNode(root.left)
    right = maxNode(root.right)
    return max(root.Data, left, right)


def height(root):
    if root is None:
        return 0
    left = height(root.left)
    right = height(root.right)
    return 1 + max(left, right)


def countLeaf(root):
    if root is None:
        return 0
    if root.left == None and root.right == None:
        return 1
    left = countLeaf(root.left)
    right = countLeaf(root.right)
    return left + right


root = treeInput()
printTree(root)
print()
printLvlWise(root)
print()
print(countNodes(root))
print(sumNodes(root))
print()
postOrder(root)
print()
inOrder(root)
print()
print(maxNode(root))
print()
print(height(root))
print()
printTree(root)
print(countLeaf(root))
