# Replace Node With Depth


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


def replaceNodeLevel(root, level=0):
    if root is None:
        return
    root.Data = level
    replaceNodeLevel(root.left, level + 1)
    replaceNodeLevel(root.right, level + 1)
    return root


root = takeInput()
printBTree(root)
level = replaceNodeLevel(root)
printBTree(level)
