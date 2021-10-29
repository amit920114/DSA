# BST Class


class BinaryTree:
    def __init__(self, data) -> None:
        self.Data = data
        self.left = None
        self.right = None


# Insert, print,count,isPresent,delete
class BST:
    def __init__(self) -> None:
        self.root = None
        self.numCount = 0

    def insertHelper(self, root, data):
        if root is None:
            root = BinaryTree(data)
            return root
        if root.Data > data:
            root.left = self.insertHelper(root.left, data)
            return root
        else:
            root.right = self.insertHelper(root.right, data)
            return root

    def insert(self, data):
        self.numCount += 1
        self.root = self.insertHelper(self.root, data)

    def printHelper(self, root):
        if root is None:
            return
        print(root.Data, end=":")
        if root.left != None:
            print("L", root.left.Data, end=",")
        if root.right != None:
            print("R", root.right.Data, end=" ")
        print()
        self.printHelper(root.left)
        self.printHelper(root.right)

    def printTree(self):
        return self.printHelper(self.root)

    def count(self):
        return self.numCount

    def isPresentHelper(self, root, data):
        if root is None:
            return False
        if root.Data == data:
            return True
        if root.Data > data:
            return self.isPresentHelper(root.left, data)
        else:
            return self.isPresentHelper(root.right, data)

    def isPresent(self, data):
        return self.isPresentHelper(self.root, data)

    def deleteHelper(self, root, data):
        if root is None:
            return False, None
        if root.Data > data:
            deleted, newLeftNode = self.deleteHelper(root.left, data)
            root.left = newLeftNode
            return deleted, root
        if root.Data < data:
            deleted, newRightNode = self.deleteHelper(root.right, data)
            root.right = newRightNode
            return deleted, root
        if root.left is None and root.right is None:
            return True, None
        if root.left is None:
            return True, root.right
        if root.right is None:
            return True, root.left
        # Root has 2 Child
        replace = self.min(root.right)
        root.Data = replace
        deleted, newRightNode = self.deleteHelper(root.right, replace)
        return True, root

    def delete(self, data):
        deleted, newNode = self.deleteHelper(self.root, data)
        if deleted:
            self.numCount -= 1
        self.root = newNode
        return deleted

    def min(self, root):
        if root is None:
            return 10000
        if root.left is None:
            return root.Data
        else:
            return self.min(root.left)


b = BST()
b.insert(4)
b.insert(2)
b.insert(6)
b.insert(7)
b.insert(1)
b.insert(3)
b.insert(5)
# b.printTree()
# print(b.count())
# print(b.isPresent(4))
print(b.delete(11))
b.printTree()
print(b.count())
print(b.isPresent(21))
