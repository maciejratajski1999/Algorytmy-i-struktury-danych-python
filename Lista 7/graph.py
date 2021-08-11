from vertex import Vertex
from graphtodot import GraphToDot
from search_algorithms import SearchAlgorithms
from topological_sort import TopologicalSort
from shortest_path import ShortestPath

class Graph:

    def __init__(self):
        self.vertices = {}

    def __contains__(self, key):
        return key in self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())

    def addVertex(self, key):
        self.vertices[key] = Vertex(key)

    def getVertex(self, key):
        return self.vertices[key]

    def addEdge(self, fromVertexKey, toVertexKey, weight=None):
        fromVertex, toVertex = self.getVertex(fromVertexKey), self.getVertex(toVertexKey)
        fromVertex.addNeighbor(toVertex, weight)

    def getVertices(self):
        return self.vertices.keys()

    def generateDot(self, file_name="graph"):
        GraphToDot(self, file_name)

    def depth_first_search(self, key):
        return SearchAlgorithms(self).depth_first_search(key)

    def breadth_first_search(self, key):
        return SearchAlgorithms(self).breadth_first_search(key)

    def topological_sort(self):
        return TopologicalSort(self).sort()

    def shortest_path(self, starting_key):
        return ShortestPath(self, starting_key).shortest_paths
