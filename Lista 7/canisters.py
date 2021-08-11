from FIFOQueue import FrontFIFOQueue as Queue

class Canister:

    def __init__(self, volume, contain=0):
        self.volume = volume
        self.contains = contain

    def fillUp(self, volume):
        space = self.volume - self.contains
        filled_volume = min([space, volume])
        new_canister = Canister(self.volume, self.contains + filled_volume)
        return new_canister, filled_volume


class TwoLitres:

    def __init__(self, first, second, parent=None):
        self.first = first
        self.second = second
        self.parent = parent

    def __eq__(self, other):
        first_equal = self.first.contains == other.first.contains
        second_equal = self.second.contains == other.second.contains
        return first_equal and second_equal

    def __str__(self):
        if self.parent is None:
            return f"<{self.first.contains}, {self.second.contains}>"
        return  str(self.parent) + "\n"+ f"<{self.first.contains}, {self.second.contains}>"

    def possibleSteps(self):
        next_steps = []
        next_steps.append(TwoLitres(self.first.fillUp(self.first.volume)[0], self.second, self))
        next_steps.append(TwoLitres(self.first, self.second.fillUp(self.second.volume)[0], self))
        next_steps.append(TwoLitres(Canister(self.first.volume), self.second, self))
        next_steps.append(TwoLitres(self.first, Canister(self.second.volume), self))
        new_second, second_fill = self.second.fillUp(self.first.contains)
        next_steps.append(TwoLitres(Canister(self.first.volume, self.first.contains - second_fill), new_second, self))
        new_first, first_fill = self.first.fillUp(self.second.contains)
        next_steps.append(TwoLitres(new_first, Canister(self.second.volume, self.second.contains - first_fill), self))
        return next_steps

    def isFinished(self, goal):
        first_finished = self.first.contains == goal
        second_finished = self.second.contains == goal
        return first_finished or second_finished


class TwoLitresGame:

    def __init__(self, first, second, goal):
        self.first, self.second, self.goal = first, second, goal

    def solve(self):
        return self.__game()

    def __game(self):
        visited = []
        state = TwoLitres(Canister(self.first),Canister(self.second))
        queue = Queue()
        queue.enqueue(state)
        visited.append(state)
        while not queue.isEmpty():
            u = queue.dequeue()
            if u.isFinished(self.goal):
                return u
            for v in u.possibleSteps():
                if not v in visited:
                    visited.append(v)
                    queue.enqueue(v)
