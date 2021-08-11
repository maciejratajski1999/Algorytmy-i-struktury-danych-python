
class BinaryHeap:

    def __init__(self, elems=[], max=None):
        if max != None:
            for i in range(0,max):
                elems = self.__get_biggest(elems)
            elems = elems[-max:]
            heap = BinaryHeap(elems)
            self.value = heap.value
            self.children = heap.children
        else:
            if elems == []:
                self.value = None
            else:
                self.levels = self.__get_size(len(elems))
                self.children_size = 2**(self.levels-1)
                self.elems = self.__get_biggest(elems)
                self.value = self.elems[-1]
                self.children = [BinaryHeap(self.elems[0:self.children_size-1]), BinaryHeap(self.elems[self.children_size-1:-1])]


    def __str__(self):
        if self.value == None:
            return str(self.value)
        else:
            return f"({self.children[0]}<- {self.value} ->{self.children[1]})"

    def __get_size(self, length):
        n = 0
        accumulate = 1
        while length >= accumulate:
            accumulate = accumulate*2
            n += 1
        return n

    def __get_biggest(self, elems):
        for i in range(0,len(elems)-1):
            if elems[i] > elems[i+1]:
                elems[i], elems[i+1] = elems[i+1], elems[i]
        return elems
