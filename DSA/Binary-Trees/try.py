# Practice Previous Concepts:-
# Tree Implementation, take input, count nodes and Sums


class BinaryTree:
    def __init__(self, data):
        self.Data = data
        self.left = None
        self.right = None


def takeInput():
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTree(rootData)
    root.left = takeInput()
    root.right = takeInput()
    return root


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


def countNodes(root):
    if root is None:
        return 0
    leftCount = countNodes(root.left)
    rightCount = countNodes(root.right)
    return leftCount + rightCount + 1


def sumOfNodes(root):
    if root is None:
        return 0
    leftSum = sumOfNodes(root.left)
    rightSum = sumOfNodes(root.right)
    return leftSum + rightSum + root.Data


# root = takeInput()
# printBTree(root)
# print(countNodes(root))
# print(sumOfNodes(root))
