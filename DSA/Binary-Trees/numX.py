# Number Of Nodes greater than X in A Binary Tree:-


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


def noOfNodesX(root, x):
    if root is None:
        return 0
    count = 0
    if root.Data > x:
        count += 1
        # return count
    left = noOfNodesX(root.left, x)
    right = noOfNodesX(root.right, x)
    return count + left + right


root = takeInput()
# printBTree(root)
# X = int(input())
print(noOfNodesX(root, 11))
