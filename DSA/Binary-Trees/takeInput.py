# Taking Input from User in Binary Tree :-


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
    leftTree = takeInputBTree()
    rightTree = takeInputBTree()
    root.left = leftTree
    root.right = rightTree
    return root


root = takeInputBTree()
printBTree(root)
