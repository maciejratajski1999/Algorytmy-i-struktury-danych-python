# zadanie 6
from unorderedlist import UnorderedList

class Stack:

    def __init__(self):
        self.content = UnorderedList()

    def pop(self):
        top = self.top.head
        self.remove(top)
        return top

    def __str__(self):
        return str(self.content)

    def push(self, item):
        self.content.add(item)

    def pop(self):
        return self.content.pop(0)

    def peek(self):
        return self.content.head()

    def isEmpty(self):
        return self.content.isEmpty()

    def size(self):
        return self.content.size()

