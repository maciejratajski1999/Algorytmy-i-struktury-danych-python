class GraphToDot:

    def __init__(self, graph, file_name):
        self.graph = graph
        self.dot_string = self.__generate_dot()
        dot_file = open(file_name+".dot", "w")
        dot_file.write(self.dot_string)
        dot_file.close()

    def __parse_vertices(self):
        connections_to_dot = []
        for vertex in self.graph.vertices.values():
                connections = [f"{vertex.key} -> {toVertex.key} [label=\"weight: {weight}\"];"
                               for toVertex, weight in vertex.connections.items()]
                for connection in connections:
                    connections_to_dot.append(connection)
        return connections_to_dot

    def __generate_dot(self):
        dot_string = "digraph prof { ratio = fill;node [style=filled];"
        connections_to_dot = self.__parse_vertices()
        for connection in connections_to_dot:
            dot_string = dot_string + "\n " + connection
        dot_string += "}"
        return dot_string
