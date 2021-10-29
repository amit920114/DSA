# Build Tree using Pre-ordwr and In-order
import queue


class BinaryTree:
    def __init__(self, data):
        self.Data = data
        self.left = None
        self.right = None


def takeInputLevelWise():
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


inorderData = []


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    # print(root.Data, end=" ")
    inorderData.append(root.Data)
    inorder(root.right)
    return inorderData


preorderData = []


def preorder(root):
    if root is None:
        return
    # print(root.Data, end=" ")
    preorderData.append(root.Data)
    preorder(root.left)
    preorder(root.right)
    return preorderData


def BTFromInPre(pre, inorder):
    if len(pre) == 0:
        return
    rootData = pre[0]
    root = BinaryTree(rootData)
    rootIndex = inorder.index(rootData)
    # rootIndex = -1
    # for k in range(0, len(inorder)):
    #     if inorder[k] == rootData:
    #         rootIndex = k
    #         break
    # if rootIndex == -1:
    #     return
    leftInorder = inorder[:rootIndex]
    rightInorder = inorder[rootIndex + 1 :]
    lenOfleftSubTree = len(leftInorder)
    leftPreOrder = pre[1 : lenOfleftSubTree + 1]
    rightPreOrder = pre[lenOfleftSubTree + 1 :]
    leftChild = BTFromInPre(leftPreOrder, leftInorder)
    rightChild = BTFromInPre(rightPreOrder, rightInorder)
    root.left = leftChild
    root.right = rightChild
    return root


def printBTree(root):
    if root is None:
        return
    print(root.Data, end=":")
    if root.left != None:
        print("L", root.left.Data, end=",")
    if root.right != None:
        print("R", root.right.Data, end="")
    print()
    printBTree(root.left)
    printBTree(root.right)


root = takeInputLevelWise()
printLevelWise(root)
print("\n")
# print("Inorder:")
inorder = inorder(root)
# print("Preorder:")
preorder = preorder(root)
rooot = BTFromInPre(preorder, inorder)
printBTree(rooot)
