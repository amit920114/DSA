class MapNode:
    def __init__(self, key, val) -> None:
        self.Key = key
        self.Value = val
        self.Next = None


class Map:
    def __init__(self) -> None:
        self.count = 0
        self.bucketSize = 10
        self.bucket = [None for k in range(self.bucketSize)]

    def size(self):
        return self.count

    def bucketIndex(self, hc):
        return abs(hc) % self.bucketSize

    def getValue(self, key):
        hc = hash(key)
        index = self.bucketIndex(hc)
        head = self.bucket[index]
        while head != None:
            if head.Key == key:
                return head.Value
            head = head.Next

        return None

    def remove(self, key):
        hc = hash(key)
        index = self.bucketIndex(hc)
        head = self.bucket[index]
        prev = None
        while head != None:
            if head.Key == key:
                if prev is None:
                    self.bucket[index] == head.Next
                else:
                    prev.Next = head.Next
                self.count -= 1
                return head.Value
            prev = head
            head = head.Next
        return None

    def insert(self, key, val):
        hc = hash(key)
        index = self.bucketIndex(hc)
        head = self.bucket[index]
        while head != None:
            if head.Key == key:
                head.Key = val
                head = head.Next
                return
        head = self.bucket[index]
        newNode = MapNode(key, val)
        newNode.Next = head
        self.bucket[index] = newNode
        self.count += 1


m = Map()
m.insert("Amit", "Kumar")
print(m.size())
m.insert("Rohit", "Sharma")
print(m.size())
m.insert("Virat", "Kohli")

print(m.size())
# m.insert("Virat", "Sharma")
# print(m.size())
print(m.getValue("Virat"))
print(m.size())
print(m.remove("Rohit"))
print(m.size())
print(m.remove("Virat"))
print(m.size())
m.insert("MS", "Dhoni")
print(m.size())
print(m.getValue("MS"))
print(m.size())
