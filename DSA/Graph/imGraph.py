# Implementation OF Graphs:-


class Graph:
    def __init__(self, nVertices) -> None:
        self.Nvertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]

    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def removeEdge(self, v1, v2):
        if self.containEdge is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def containEdge(self, v1, v2):
        return True if self.adjMatrix[v1][v2] > 0 else False

    def __str__(self) -> str:
        return str(self.adjMatrix)


g = Graph(4)
g.addEdge(0, 3)
g.addEdge(2, 2)
g.addEdge(2, 0)
print(g)
