# Check if Tree is Binary Search Tree or No:
import queue


class BInaryTree:
    def __init__(self, data) -> None:
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


def minTree(root):
    if root is None:
        return 100000
    leftMin = minTree(root.left)
    rightMin = minTree(root.right)
    return min(leftMin, rightMin, root.Data)


def maxTree(root):
    if root is None:
        return -100000
    leftMax = maxTree(root.left)
    rightMax = maxTree(root.right)
    return max(leftMax, rightMax, root.Data)


def isBST(root):
    if root is None:
        return True
    leftMax = maxTree(root.left)
    rightMin = minTree(root.right)
    if rightMin < root.Data or leftMax >= root.Data:
        return False
    leftBSt = isBST(root.left)
    rightBst = isBST(root.right)
    return leftBSt and rightBst


def isBSTV2(root):
    if root is None:
        return 100000, -100000, True
    leftMin, leftMax, leftBst = isBSTV2(root.left)
    rightMin, rightMax, rightBst = isBSTV2(root.right)

    minimum = min(leftMin, rightMin, root.Data)
    maximum = max(leftMax, rightMax, root.Data)
    Isbst = True
    if root.Data > rightMin or root.Data <= leftMax:
        Isbst = False
    if not (leftBst) or not (rightBst):
        Isbst = False
    return minimum, maximum, Isbst


def isBstV3(root, minRange, maxRange):
    if root is None:
        return True
    if root.Data > maxRange or root.Data < minRange:
        return False
    bstLeft = isBstV3(root.left, minRange, root.Data - 1)
    bstright = isBstV3(root.right, root.Data, maxRange)
    return bstLeft and bstright


root = takeInput()
prinBt(root)
print(isBSTV2(root))
# print(isBstV3(root, -100000, 100000))
