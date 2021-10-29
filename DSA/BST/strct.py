# Structure of BST
# Class of BST


class BinaryTree:
    def __init__(self, data):
        self.Data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.numCount = 0

    def isPresenthelper(self, root, data):
        if root is None:
            return False
        if root.Data == data:
            return True
        if root.Data > data:
            # Check for left
            return self.isPresenthelper(root.left, data)
        else:
            # Check for right
            return self.isPresenthelper(root.right, data)

    def isPresent(self, data):
        return self.isPresenthelper(self.root, data)

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

    def insertHelper(self, root, data):
        if root is None:
            node = BinaryTree(data)
            return node
        if root.Data > data:
            root.left = self.insertHelper(root.left, data)
            return root
        else:
            root.right = self.insertHelper(root.right, data)
            return root

    def insert(self, data):
        self.numCount += 1
        self.root = self.insertHelper(self.root, data)

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
        #  if root has no childrem]n
        if root.left is None and root.right is None:
            return True, None
        # Only right child
        if root.left is None:
            return True, root.right
        # Only Left Child
        if root.right is None:
            return True, root.left
        # Root has two children
        replacement = self.min(root.right)
        root.Data = replacement
        deleted, newRightNode = self.deleteHelper(root.right, replacement)
        root.right = newRightNode
        return True, root

    def min(self, root):
        if root is None:
            return 1000000
        if root.left is None:
            return root.Data
        return self.min(root.left)

    def delete(self, data):
        deleted, newRoot = self.deleteHelper(self.root, data)
        if deleted:
            self.numCount -= 1
        self.root = newRoot
        return deleted

    # def countHelper(self, root):
    #     if root is None:
    #         return 0
    #     return self.countHelper(root.left) + self.countHelper(root.right) + 1

    def count(self):
        return self.numCount


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
# print(b.isPresent(7))
print(b.delete(20))
b.printTree()
print(b.count())
print(b.isPresent(99))
