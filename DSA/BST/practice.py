# Practice Is BST:-
import queue


class BinaryTree:
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


# def printBt(root):
#     q = queue.Queue()
#     if root is None:
#         return
#     print(root.Data, end=" ")
#     q.put(root)
#     while not (q.empty()):
#         currentNode = q.get()
#         if currentNode.left != None:
#             print(currentNode.left.Data, end=" ")
#             q.put(currentNode.left)
#         if currentNode.right != None:
#             print(currentNode.right.Data, end=" ")
#             q.put(currentNode.right)
def printBt(root):
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


def Bst(root):
    if root is None:
        return -100000, 100000, True
    leftMax, leftMin, isBstLeft = Bst(root.left)
    rightMax, rightMin, ISBstright = Bst(root.right)

    maximum = max(leftMax, rightMax, root.Data)
    minimum = min(leftMin, rightMin, root.Data)
    isBst = True
    if root.Data > rightMin or root.Data <= leftMax:
        isBst = False
    if not (isBstLeft) or not (ISBstright):
        isBst = False
    return maximum, minimum, isBst


root = takeInput()
printBt(root)
print(Bst(root))
