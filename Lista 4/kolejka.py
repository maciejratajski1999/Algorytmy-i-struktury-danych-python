#zadanie 1
import unittest
import time

class FrontFIFOQueue:
#koniec kolejki na początku listy
    def __init__(self):
        self.queue = []

    def enqueue(self, new):
        self.queue.insert(0, new)

    def dequeue(self):
        return self.queue.pop()

    def isEmpty(self):
        return self.size()==0

    def size(self):
        return len(self.queue)

class BackwardFIFOQueue:
#koniec kolejki na końcu listy
    def __init__(self):
        self.queue = []

    def enqueue(self, new):
        self.queue.append(new)

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("this Queue is empty")
        return self.queue.pop(0)

    def isEmpty(self):
        return self.size()==0

    def size(self):
        return len(self.queue)

# zadanie 2
if __name__ == "__main__":
    tries = 100000

    print("testing for Front FIFO Queue: ")
    front = FrontFIFOQueue()
    timer = time.time()
    for i in range(0,tries):
        front.enqueue(i)
    for i in range(0,tries):
        front.dequeue()
    print(time.time() - timer)

    print("testing for Backward FIFO Queue: ")
    backward = BackwardFIFOQueue()
    timer = time.time()
    for i in range(0, tries):
        backward.enqueue(i)
    for i in range(0, tries):
        backward.dequeue()
    print(time.time() - timer)


