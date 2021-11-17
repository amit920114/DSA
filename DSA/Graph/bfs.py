# Implementation of BFS: Breadth First Search
import queue


class Graph:
    def __init__(self, nVertices) -> None:
        self.Nvertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]

    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def containEdge(self, v1, v2):
        return True if self.adjMatrix[v1][v2] > 0 else False

    def removeEdge(self, v1, v2):
        if self.containEdge is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def __str__(self) -> str:
        return self.adjMatrix

    def bfs(self):
        q = queue.Queue()
        q.put(0)
        visited = [False for i in range(self.Nvertices)]
        visited[0] = True
        while not q.empty():
            val = q.get()
            print(val)
            for i in range(self.Nvertices):
                if self.adjMatrix[i][val] > 0 and visited[i] is False:
                    q.put(i)
                    visited[i] = True


g = Graph(7)
g.addEdge(0, 1)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(0, 2)
g.addEdge(4, 5)
g.addEdge(2, 6)
g.addEdge(5, 6)
g.bfs()
