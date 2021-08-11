from node import Node

# zadanie 5
class UnorderedList:

    def __init__(self, top=None):
        self.top = top

    def __str__(self):
        return str(self.top)

    def head(self):
        return self.top.head

    def isEmpty(self):
        return self.top == None

    def add(self, item):
        self.top = Node(item, self.top)

    def append(self, item):
        temp = self.top
        if temp ==  None:
            self.add(item)
            return
        while temp != None:
            prev = temp
            temp = temp.tail
        prev.tail = Node(item)

    def size(self):
        n = 0
        temp = self.top
        while temp != None:
            n += 1
            temp = temp.tail
        return n

    def search(self, item):
        if self.isEmpty():
            return False
        temporary = self.top
        if temporary.head != item:
            return UnorderedList(self.top.tail).search(item)
        return True

    def remove(self, item, previous=None):
        temporary = self.top

        if self.isEmpty():
            return
        if temporary.head != item:
            previous = temporary
            UnorderedList(self.top.tail).remove(item, previous)

        if previous == None:
            self.top = temporary.tail
        else:
            previous.tail = temporary.tail

    def pop(self, pos=None):
        try:
            if pos == None:
                pos = self.size() - 1
            if pos == 0:
                top = self.top.head
                self.top = self.top.tail
                return top
            else:
                temp = self.top
                counter = 0
                while counter != pos:
                    counter+=1
                    prev = temp
                    temp = temp.tail
                prev.tail = temp.tail
                return temp.head
        except AttributeError:
            raise IndexError(f"Given index: {pos} is too big for this list")

    def insert(self, pos, item):
        if pos == 0:
            self.add(item)
        else:
            try:
                counter = 0
                temp = self.top
                while counter != pos:
                    counter += 1
                    prev = temp
                    temp = temp.tail

                prev.tail = Node(item, temp)
            except AttributeError:
                raise IndexError(f"Given index: {pos} is too big for this list")

    def index(self, item):
        counter = 0
        temp = self.top
        try:
            while temp.head != item:
                counter += 1
                temp = temp.tail
            return counter
        except AttributeError:
            raise ValueError(f"Item  {item} not in list")


# zadanie 8
if __name__ == "__main__":
    import time
    tries = 5000

    print("testing for UnorderedList: ")
    timer = time.time()
    unordered_list = UnorderedList()
    for i in range(0, tries):
        unordered_list.add(i)
    for i in range(0, tries):
        unordered_list.pop()
    print(time.time() - timer)

    print("testing for Python list: ")
    timer = time.time()
    python_list = []
    for i in range(0, tries):
        python_list.insert(0,i)
    for i in range(0, tries):
        python_list.pop()
    print(time.time() - timer)
