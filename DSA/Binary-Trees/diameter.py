# Find The Diameter of A Binary Tree:-


class BinaryTree:
    def __init__(self, data):
        self.Data = data
        self.left = None
        self.right = None


def printBT(root):
    if root is None:
        return
    print(root.Data, end=":")
    if root.left != None:
        print("L", root.left.Data, end=",")
    if root.right != None:
        print("R", root.right.Data, end="")
    print()
    printBT(root.left)
    printBT(root.right)


def takeInput():
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTree(rootData)
    root.left = takeInput()
    root.right = takeInput()
    return root


def diameterBT(root):
    if root is None:
        return 0, 0
    LH, leftDH = diameterBT(root.left)
    RH, rightDH = diameterBT(root.right)
    h = 1 + max(LH, RH)
    opt1 = LH + RH
    return h, max(opt1, leftDH, rightDH)


root = takeInput()
printBT(root)
print(diameterBT(root))
