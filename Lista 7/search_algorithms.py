from FIFOQueue import FrontFIFOQueue as Queue
class SearchAlgorithms:

    def __init__(self, graph):
        self.graph = graph

    def depth_first_search(self, key):

        def recursive_search(current_vertex):
            current_vertex.setColor("black")
            if current_vertex.key == key:
                return True
            for neighbor_vertex in current_vertex.connections.keys():
                if neighbor_vertex.color == "white":
                    return recursive_search(neighbor_vertex)
            return False

        for vertex in self.graph.vertices.values():
            vertex.setColor("white")
        for vertex in self.graph.vertices.values():
            if vertex.color == "white":
                if recursive_search(vertex):
                    return True
        return False

    def breadth_first_search(self, key):
        for vertex in self.graph.vertices.values():
            vertex.setColor("white")
        for current in self.graph.vertices.values():
            if current.color == "white":
                current.setColor("grey")
                queue = Queue()
                queue.enqueue(current)
                while not queue.isEmpty():
                    u = queue.dequeue()
                    if u.key == key:
                        return True
                    for v in u.connections.keys():
                        if v.color == "white":
                            v.setColor("grey")
                            queue.enqueue(v)
                    u.setColor("black")
                return False
