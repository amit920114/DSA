# Calculate the height of a Tree:-


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


def heiOfTree(root):
    if root is None:
        return 0
    left = heiOfTree(root.left)
    right = heiOfTree(root.right)
    if left > right:
        return 1 + left
    else:
        return 1 + right


root = takeInput()
printBT(root)
print(heiOfTree(root))
