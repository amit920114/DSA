# Count number of Leaf Nodes:-


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


def leafNodes(root):
    if root is None:
        return 0
    if root.left == None and root.right == None:
        return 1
    left = leafNodes(root.left)
    right = leafNodes(root.right)
    return left + right


root = takeInput()
printBT(root)
print(leafNodes(root))
