# IS Node Present Or not
class BinaryTree:
    def __init__(self, data):
        self.Data = data
        self.left = None
        self.right = None


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


def takeInput():
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTree(rootData)
    root.left = takeInput()
    root.right = takeInput()
    return root


def isNode(root, x):
    if root is None:
        return False
    if root.Data == x:
        return True
    left = isNode(root.left, x)
    if left:
        return True
    right = isNode(root.right, x)
    return right


root = takeInput()
printBTree(root)
if isNode(root, 52):
    print("True")
else:
    print("False")
