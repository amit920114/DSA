# implementation Of Generic Tree:-
import queue


class GT:
    def __init__(self, data) -> None:
        self.Data = data
        self.Children = []


def gtInput():
    q = queue.Queue()
    print("Enter root")
    rootData = int(input())
    if rootData == -1:
        return
    root = GT(rootData)
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        print("Enter number of children of", currentNode.Data)
        numChild = int(input())
        for child in range(numChild):
            print("Enter next Child of ", currentNode.Data)
            childData = int(input())
            child = GT(childData)
            currentNode.Children.append(child)
            q.put(child)
    return root


def printGT(root):
    if root is None:
        return
    print(root.Data, end=": ")
    for child in root.Children:
        print(child.Data, end=",")
    print()
    for child2 in root.Children:
        printGT(child2)


def printLvl(root):
    q = queue.Queue()
    if root is None:
        return
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        print(currentNode.Data, end=" ")
        for child in currentNode.Children:
            q.put(child)


def countGT(root):
    if root is None:
        return 0
    count = 1
    for child in root.Children:
        count = count + countGT(child)
    return count


def heightGT(root):
    if root is None:
        return 0
    height = 0
    for child in root.Children:
        childHeight = heightGT(child)
        height = max(childHeight, height)
    return height + 1


def sumNodes(root):
    if root is None:
        return 0
    sum = root.Data
    for child in root.Children:
        sum = sum + sumNodes(child)

    return sum


def maxNode(root):
    if root is None:
        return
    maxND = root.Data
    for child in root.Children:
        maxChild = maxNode(child)
        maxND = max(maxChild, maxND)

    return maxND


def nextLgr(root, n):
    if root is None:
        return
    ans = -1
    if root.Data > n:
        ans = root.Data

    for child in root.Children:
        temp = nextLgr(child, n)
        if ans == -1:
            ans = temp
        ans = min(temp, ans)
    return ans


def replceDepth(root, depth):
    if root is None:
        return
    i = 0
    root.Data = depth
    while i < len(root.Children):
        replceDepth(root.Children[i], depth + 1)
        i += 1
    return root


root = gtInput()
printGT(root)
printLvl(root)
print()
# print(countGT(root))
# print(heightGT(root))
# print(sumNodes(root))
# print(maxNode(root))
# print(nextLgr(root, 10))
ans = replceDepth(root, 0)
printGT(ans)
printLvl(ans)
