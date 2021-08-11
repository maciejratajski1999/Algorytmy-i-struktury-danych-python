from FIFOQueue import FrontFIFOQueue as Queue

class MissionariesCannibals:

    def __init__(self, missionaries, cannibals, boat_side, parent=None):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat_side = boat_side
        self.parent = parent

    def __eq__(self, other):
        m = self.missionaries == other.missionaries
        c = self.cannibals == other.cannibals
        b = self.boat_side == other.boat_side
        return m and c and b

    def __str__(self):
        if self.parent is None:
            return f"<{self.missionaries}, {self.cannibals}, {self.boat_side}>" + "\n"
        return str(self.parent) + f"<{self.missionaries}, {self.cannibals}, {self.boat_side}>" + "\n"

    def isValid(self):
        if not self.missionaries in [0,1,2,3]:
            return False
        if not self.cannibals in [0,1,2,3]:
            return False
        if (self.missionaries > 0):
            if self.missionaries < self.cannibals:
                return False
        rm, rc = 3-self.missionaries, 3-self.cannibals
        if rm > 0:
            if rm < rc:
                return False
        return True

    def possibleSteps(self):
        possible_steps = []
        if self.boat_side == 1:
            next_boat_side = 0
            steps = [[0,-1],[0,-2],[-1,-1],[-1,0],[-2,0]]
        else:
            next_boat_side = 1
            steps = [[0, 1], [0, 2], [1, 1], [1, 0], [2, 0]]
        for step in steps:
            next_missionaries = self.missionaries + step[0]
            next_cannibals = self.cannibals + step[1]
            next_state = MissionariesCannibals(next_missionaries, next_cannibals, next_boat_side, self)
            if next_state.isValid():
                possible_steps.append(next_state)
        return possible_steps




class RiverCrossing:

    def __init__(self):
        self.result = self.__game()

    def __next_step(self, step):
        pass

    def __game(self):
        visited = []
        state = MissionariesCannibals(3, 3, 1)
        queue = Queue()
        queue.enqueue(state)
        visited.append(state)
        while not queue.isEmpty():
            u = queue.dequeue()
            if u == MissionariesCannibals(0,0,0):
                return u
            for v in u.possibleSteps():
                if not v in visited:
                    visited.append(v)
                    queue.enqueue(v)

