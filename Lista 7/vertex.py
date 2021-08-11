class Vertex:

    def __init__(self, key):
        self.key = key
        self.connections = {}
        self.color = 'white'
        self.found_time = None
        self.leave_time = None

    def __str__(self):
        return str(self.key) + " --> " + str([vertex.key for vertex in self.connections.keys()])

    def addNeighbor(self, neighbor, weight=None):
        self.connections[neighbor] = weight

    def getConnections(self):
        return self.connections

    def setColor(self, color):
        self.color = color

    def setFoundTime(self, time):
        self.found_time = time

    def setLeaveTime(self, time):
        self.leave_time = time

    def getId(self):
        return self.key

    def getWeight(self, neighbor):
        return self.connections[neighbor]
