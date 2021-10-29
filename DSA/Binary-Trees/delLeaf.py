# Delete Leaf Nodes:-


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


def removeLeaf(root):
    if root is None:
        return None
    if root.left == None and root.right == None:
        return None
    root.left = removeLeaf(root.left)
    root.right = removeLeaf(root.right)
    return root


root = takeInput()
printBTree(root)
removeLeaf(root)
print("#" * 10)
printBTree(root)
