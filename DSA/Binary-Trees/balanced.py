# Check If Binary Tree is Balanced OR Not


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


def isBalanced(root):
    if root is None:
        return True
    leftH = heightBT(root.left)
    rightH = heightBT(root.right)
    if leftH - rightH > 1 or rightH - leftH > 1:
        return False
    left = isBalanced(root.left)
    right = isBalanced(root.right)
    if left and right:
        return True
    else:
        return False


def isBalancedAndHeight(root):
    if root is None:
        return 0, True
    LH, leftBalanced = isBalancedAndHeight(root.left)
    RH, rightBalanced = isBalancedAndHeight(root.right)
    h = 1 + max(LH, RH)
    if LH - RH > 1 or RH - LH > 1:
        return h, False
    if leftBalanced and rightBalanced:
        return h, True
    else:
        return h, False


def heightBT(root):
    if root is None:
        return 0
    return 1 + max(heightBT(root.left), heightBT(root.right))


root = takeInput()
printBT(root)
# print(isBalanced(root))
print(isBalancedAndHeight(root))
