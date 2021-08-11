from FIFOQueue import FrontFIFOQueue as Queue
class ShortestPath:

    def __init__(self, graph, starting_key):
        self.graph = graph
        self.start = starting_key
        self.shortest_paths = {}
        self.__breadth_first_search(self.start)

    def __breadth_first_search(self, current_key):
        current_vertex = self.graph.vertices[current_key]
        self.shortest_paths[current_key] = [current_key]
        queue = Queue()
        queue.enqueue(current_vertex)
        while not queue.isEmpty():
            u = queue.dequeue()
            path = self.shortest_paths[u.key]
            for v in u.connections.keys():
                if not v.key in self.shortest_paths.keys():
                    self.shortest_paths[v.key] = path + [v.key]
                    queue.enqueue(v)

