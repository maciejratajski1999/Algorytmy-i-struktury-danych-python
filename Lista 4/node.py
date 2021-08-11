class Node:

    def __init__(self, head, tail=None):
        self.head = head
        self.tail = tail

    def __str__(self):
        return str(self.head) + " -> " + str(self.tail)

    def head(self):
        return self.head

    def tail(self):
        return self.tail
