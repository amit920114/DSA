# Build BST From an Sorted Array
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


def bstArr(arr):
    if len(arr) == 0:
        return
    mid = (len(arr)) // 2
    rootData = arr[mid]
    root = BinaryTree(rootData)
    root.left = bstArr(arr[:mid])
    root.right = bstArr(arr[mid + 1 :])
    return root


def printBt(root):
    if root is None:
        return
    print(root.Data, end=":")
    if root.left != None:
        print("L", root.left.Data, end=",")
    if root.right != None:
        print("R", root.right.Data, end=" ")
    print()
    printBt(root.left)
    printBt(root.right)


# root = takeInput()
# printBt(root)
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
root = bstArr(arr)
printBt(root)
