# Printing Binary Tree


class BinaryTree:
    def __init__(self, data):
        self.Data = data
        self.left = None
        self.right = None


def printBinaryTree(root):
    if root is None:
        return
    print(root.Data, end=":")
    if root.left != None:
        print("L", root.left.Data, end=",")
    if root.right != None:
        print("R", root.right.Data, end="")
    print()
    printBinaryTree(root.left)
    printBinaryTree(root.right)


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


# btn1 = BinaryTree(10)
# btn2 = BinaryTree(75)
# btn3 = BinaryTree(49)
# btn4 = BinaryTree(23)
# btn5 = BinaryTree(45)
# btn6 = BinaryTree(52)

# btn1.left = btn2
# btn1.right = btn3
# btn2.left = btn4
# btn2.right = btn5
# btn3.left = btn6


root = takeInputBTree()
# printBinaryTree(root)
