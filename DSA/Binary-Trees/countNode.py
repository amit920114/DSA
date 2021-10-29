# Count Number of Nodes in a Binary Tree:-


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


def takeInputBTree():
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTree(rootData)
    root.left = takeInputBTree()
    root.right = takeInputBTree()
    return root


# Count The number of Nodes of B'Tree


def countNodes(root):
    if root is None:
        return 0
    leftCount = countNodes(root.left)
    rightCount = countNodes(root.right)
    return leftCount + rightCount + 1


root = takeInputBTree()
printBTree(root)
print(countNodes(root))
