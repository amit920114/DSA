# Build Bianry Tree using Post Order and Inoder

# a = [1, 2, 3, 4, 5, 6, 7]
# b = a[:-1]
# print(b)
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
        print("Enter left Child of ", currentNode.Data)
        leftChildData = int(input())
        if leftChildData != -1:
            leftChild = BinaryTree(leftChildData)
            currentNode.left = leftChild
            q.put(leftChild)
        print("Enter right child of ", currentNode.Data)
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


postorderData = []


def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    postorderData.append(root.Data)
    return postorderData


inorderData = []


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    inorderData.append(root.Data)
    inorder(root.right)
    return inorderData


def postInorderBT(post, inorder):
    if len(post) == 0:
        return
    rootData = post[-1]
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
    lenghtOfLeftInorder = len(leftInorder)
    leftPostOrder = post[: lenghtOfLeftInorder + 1]
    rightPostorder = post[lenghtOfLeftInorder + 1 : -1]
    leftChild = postInorderBT(leftPostOrder, leftInorder)
    righChild = postInorderBT(rightPostorder, rightInorder)
    root.left = leftChild
    root.right = righChild
    return rootData


root = takeInputLevelWise()
printLevelWise(root)
print(" ")
postorder = postorder(root)
print(postorder)
inorder = inorder(root)
print(inorder)
printBt(root)
print(" ")
rooot = postInorderBT(postorder, inorder)
print("Tree using PostOrder and Inorder")
printBt(rooot)
