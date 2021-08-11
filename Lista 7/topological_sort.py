
class TopologicalSort:

    def __init__(self, graph):
        self.graph = graph
        self.time = 1
        for vertex in graph.vertices.values():
            vertex.setColor('white')

    def __timer(self):
        self.time += 1

    def __depth_first_search(self, key, start, path=[]):
        path.append(start)
        current = self.graph.vertices[start]
        current.setColor('grey')
        current.setFoundTime(self.time)
        self.__timer()
        if key == start:
            return path
        for vertex in current.connections.keys():
            if vertex.color == 'black':
                continue
            elif vertex.key in path:
                raise ValueError("I've encountered a cycle! Oops!")
            else:
                further = self.__depth_first_search(key, vertex.key, path)
                if further == None:
                    continue
                else:
                    return further
        current.setLeaveTime(self.time)
        self.__timer()
        current.setColor('black')

    def sort(self, start=None):
        if start == None:
            start = list(self.graph.vertices.keys())[0]
        self.__depth_first_search(None, start)
        for vertex in self.graph.vertices.values():
            if vertex.color == 'white':
                self.__depth_first_search(None, vertex.key)
        vertices_by_time = {vertex.leave_time:vertex.key for vertex in self.graph}
        times_sorted = sorted(vertices_by_time.keys(), reverse=True)
        return [vertices_by_time[t] for t in times_sorted]




