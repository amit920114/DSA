# Sum Of Nodes In a Binary Tree:-


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


def sumOfNodes(root):
    if root is None:
        return 0
    sumLeft = sumOfNodes(root.left)
    sumRight = sumOfNodes(root.right)
    return sumLeft + sumRight + root.Data


root = takeInput()
printBTree(root)
print("Sum of Nodes:- ", sumOfNodes(root))
