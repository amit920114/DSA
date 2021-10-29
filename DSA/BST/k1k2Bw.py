# Finding Nodes bw K1 and K2 in Binary Search Tree:-
import queue


class BinaryTree:
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


# --------------Self---------------
def rangeV1(root, k1, k2):
    if root is None:
        return
    if root.Data <= k1:
        # print(root.Data, end=" ")
        return rangeV1(root.right, k1, k2)
    print(root.Data, end=" ")
    if root.Data >= k2:
        return rangeV1(root.left, k1, k2)
    else:
        # print(root.Data, end=" ")
        rangeV1(root.left, k1, k2)
        rangeV1(root.right, k1, k2)


# ------------------------------------------
def range(root, k1, k2):
    if root is None:
        return
    if root.Data < k1:
        range(root.right, k1, k2)
    elif root.Data > k2:
        range(root.left, k1, k2)
    else:
        print(root.Data, end=" ")
        range(root.left, k1, k2)
        range(root.right, k1, k2)


root = takeInput()
printBT(root)
print("--------")
btwK1K2 = range(root, 6, 10)
printBT(btwK1K2)
