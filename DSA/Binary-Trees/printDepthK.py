# Print The Nodes after the k NOdes:-
# Print Depth of K


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


def depthK(root, k):
    if root is None:
        return
    if k == 0:
        print(root.Data, end=" ")
        return
    depthK(root.left, k - 1)
    depthK(root.right, k - 1)


def depthkV2(root, k, d=0):
    if root is None:
        return
    if k == d:
        print(root.Data, end=" ")
    depthkV2(root.left, k, d + 1)
    depthkV2(root.right, k, d + 1)


root = takeInput()
printBTree(root)
# depthK(root, 0)
depthkV2(root, 1)
