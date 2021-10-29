# Find The Largest Data in BinaryTree:-


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


def largestData(root):
    if root is None:
        return -1
    return max(largestData(root.left), largestData(root.right), root.Data)


root = takeInput()
print("Largest Number is:- ", largestData(root))
