from unorderedlist import UnorderedList

#zadanie 7
class Deque:

    def __init__(self):
        self.queue = UnorderedList()

    def addFront(self, item):
        self.queue.add(item)

    def addRear(self, item):
        self.queue.append(item)

    def removeFront(self):
        if self.isEmpty():
            raise IndexError("this Queue is empty")
        return self.queue.pop(0)

    def removeRear(self):
        if self.isEmpty():
            raise IndexError("this Queue is empty")
        return self.queue.pop()

    def isEmpty(self):
        return self.queue.isEmpty()

    def size(self):
        return self.queue.size()
