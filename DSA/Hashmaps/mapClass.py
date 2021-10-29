# Map Class
class MapNode:
    def __init__(self, key, value) -> None:
        self.Key = key
        self.Value = value
        self.Next = None


class Map:
    def __init__(self) -> None:
        self.bucketSize = 10
        self.buckets = [None for k in range(self.bucketSize)]
        self.count = 0

    def size(self):
        return self.count

    def bucketIndex(self, hc):
        return abs(hc) % (self.bucketSize)

    def getValue(self, key):
        hc = hash(key)
        index = self.bucketIndex(hc)
        head = self.buckets[index]
        while head != None:
            if head.Key == key:
                return head.Value
        head = head.Next
        return None

    def remove(self, key):
        hc = hash(key)
        index = self.bucketIndex(hc)
        head = self.buckets[index]
        prev = None
        while head != None:
            if head.Key == key:
                if prev is None:
                    self.buckets[index] = head.Next
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
        head = self.buckets[index]
        while head != None:
            if head.Key == key:
                head.Value = val
                return
            head = head.Next
        head = self.buckets[index]
        newNode = MapNode(key, val)
        newNode.Next = head
        self.buckets[index] = newNode
        self.count += 1


map = Map()
map.insert("Amit", 22)
print(map.size())
map.insert("Anil", 33)
print(map.size())
map.insert("Sujay", "48")
print(map.size())
# map.insert("Sujay", "45")
# print(map.size())
print(map.getValue("Sujay"))
print(map.size())
print(map.remove("Sujay"))
print(map.size())
