class MapNode:
    def __init__(self, key, value) -> None:
        self.Key = key
        self.Value = value
        self.Next = None


class Map:
    def __init__(self) -> None:
        self.count = 0
        self.bucketSize = 5
        self.bucket = [None for k in range(self.bucketSize)]

    def size(self):
        return self.count

    def bucketIndex(self, hc):
        return abs(hc) % self.bucketSize

    def rehash(self):
        temp = self.bucket
        self.bucket = [None for k in range(2 * self.bucketSize)]
        self.bucketSize = 2 * self.bucketSize
        self.count = 0
        for head in temp:
            while head != None:
                self.insert(head.Key, head.Value)
                head = head.Next

    def insert(self, key, val):
        hc = hash(key)
        index = self.bucketIndex(hc)
        head = self.bucket[index]
        while head != None:
            if head.Key == key:
                head.Key = val
                return
            head = head.Next
        head = self.bucket[index]
        newNode = MapNode(key, val)
        newNode.Next = head
        self.bucket[index] = newNode
        self.count += 1
        loadFactor = self.count / self.bucketSize
        if loadFactor >= 0.7:
            self.rehash()

    def getValue(self, key):
        hc = hash(key)
        index = self.bucketIndex(hc)
        head = self.bucket[index]
        while head != None:
            if head.Key == key:
                return head.Value
            head = head.Next
        return None

    def loadFactor(self):
        return self.count / self.bucketSize

    def remove(self, key):
        hc = hash(key)
        index = self.bucketIndex(hc)
        head = self.bucket[index]
        prev = None
        while head != None:
            if head.Key == key:
                if prev is None:
                    self.bucket[index] = head.Next
                else:
                    prev.Next = head.Next
                return head.Value
            prev = head
            head = head.Next
        return None


m = Map()
arr = [9, 1, 8, 6, 3, 4, 2, 7, 10, 15]
# for i in range(10):
#     m.insert("Amit" + str(i), i + 1)
#     print(m.loadFactor())
for i in arr:
    m.insert(i, True)
#
for i in arr:
    print(i, m.getValue(i))
# print(m.getValue(6))
