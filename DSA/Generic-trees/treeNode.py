# Generic Trees:-
# :- Intro, PritTree, TakeInput, Count, height, Sum
import queue


class GenericTree:
    def __init__(self, data) -> None:
        self.Data = data
        self.Children = list()


n1 = GenericTree(5)
n2 = GenericTree(7)
n3 = GenericTree(9)
n4 = GenericTree(11)
n5 = GenericTree(21)
n6 = GenericTree(6)
n7 = GenericTree(2)

n1.Children.append(n2)
n1.Children.append(n3)
n1.Children.append(n4)
n1.Children.append(n5)

n3.Children.append(n6)
n3.Children.append(n7)
# print(n3.Children[1].Data)
def printTree(root):
    # Edge Case not an Base Case
    if root is None:
        return
    print(root.Data)
    for child in root.Children:
        printTree(child)


# ------------In A Proper Way ------------- #
def PrintBetter(root):
    if root is None:
        return
    print(root.Data, end=" :")
    for child in root.Children:
        print(child.Data, end=",")
    print()
    for child2 in root.Children:
        PrintBetter(child2)


# -----------Take Input-------------#


def takeInput():
    print("Enter root Data")
    rootData = int(input())
    if rootData == -1:
        return
    root = GenericTree(rootData)
    print("Enter number of children of", rootData)
    numChildren = int(input())
    for child in range(numChildren):
        child = takeInput()
        root.Children.append(child)

    return root


def countNodes(root):
    if root is None:
        return 0
    count = 1
    for child in root.Children:
        count = count + countNodes(child)
    return count


def heightOfGT(root):
    # height = 0
    if root is None:  # edge case
        return 0
    height = 0
    for child in root.Children:
        childHeight = heightOfGT(child)
        height = max(height, childHeight)
    return height + 1


def sumGT(root):
    # sum = 0
    if root is None:
        return 0
    sum = 0
    for child in root.Children:
        childSum = sumGT(child)
        sum = sum + childSum
    return sum + root.Data


def maxNode(root):
    # edge case
    if root is None:
        return 0
    maxi = root.Data
    for child in root.Children:
        childMax = maxNode(child)
        maxi = max(maxi, childMax)
    return maxi


def inputLevelWise():
    q = queue.Queue()
    print("Enter root")
    rootData = int(input())
    if rootData == -1:
        return
    root = GenericTree(rootData)
    q.put(root)
    while not (q.empty()):
        currentNode = q.get()
        print("Enter number of childrens of", currentNode.Data)
        numChild = int(input())
        for i in range(numChild):
            print("Enter next child of", currentNode.Data)
            childData = int(input())
            child = GenericTree(childData)
            currentNode.Children.append(child)
            q.put(child)
    return root


def printLevelWise(root):
    q = queue.Queue()
    if root is None:
        return
    q.put(root)
    while not (q.empty()):
        currentNode = q.get()
        print(currentNode.Data, end=" ")
        for child in currentNode.Children:
            q.put(child)


# printTree(n1)
# PrintBetter(n1)
# root = takeInput()
root = inputLevelWise()
printLevelWise(root)
print()
PrintBetter(root)
# print(countNodes(root))
print(heightOfGT(root))
print(sumGT(root))
print("Maximimum")
print(maxNode(root))
