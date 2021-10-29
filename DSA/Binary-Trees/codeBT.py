# Creating Binary Trees
# Generic Tree: Tree that have n numbers of childerns are known to be Generic Trees.
# Binary Tree: Tree that have only 0 or 1 or 2 childerens are known to be Binary Trees.


class BinaryTrees:
    def __init__(self, data):
        self.Data = data
        self.left = None
        self.right = None


btn1 = BinaryTrees(10)
btn2 = BinaryTrees(29)
btn3 = BinaryTrees(45)
btn4 = BinaryTrees(79)
btn5 = BinaryTrees(13)


def printTree(root):
    if root is None:
        return
    print(root.Data, end=":")
    if root.left != None:
        print("L", root.left.Data, end=",")
    if root.right != None:
        print("R", root.right.Data, end="")
    print()
    printTree(root.left)
    printTree(root.right)


btn1.left = btn2
btn1.right = btn3
btn2.left = btn4
btn2.right = btn5
printTree(btn1)
