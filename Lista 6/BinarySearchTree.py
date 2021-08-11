class BinarySearchTree:

    def __init__(self, value=None):
        self.value = value
        self.children = []
        if self.value != None:
            self.children = [BinarySearchTree(),BinarySearchTree()]


    def __str__(self):
        if self.value == None:
            return str(self.value)
        else:
            return f"({self.children[0]}<- {self.value} ->{self.children[1]})"

    def insert(self, new_value):
        if self.value == None:
            self.value = new_value
            self.children = [BinarySearchTree(),BinarySearchTree()]
        else:
            if new_value == self.value:
                return
            elif new_value < self.value:
                if self.children[0].value == None:
                    self.children[0] = BinarySearchTree(new_value)
                else:
                    self.children[0].insert(new_value)
            elif new_value > self.value:
                if self.children[1].value == None:
                    self.children[1] = BinarySearchTree(new_value)
                else:
                    self.children[1].insert(new_value)

    def deletion(self, value):
        if self.value != None:
            if value == self.value:
                left_tree = self.children[0]
                self.value = self.children[1].value
                self.children = self.children[1].children
                self.insert_tree(left_tree)
            elif value < self.value:
                self.children[0].deletion(value)
            elif value > self.value:
                self.children[1].deletion(value)
        else:
            return


    def insert_all(self, elements):
        for element in elements:
            self.insert(element)

    def insert_tree(self, tree):
        if tree.value != None:
            self.insert(tree.value)
            self.insert_tree(tree.children[0])
            self.insert_tree(tree.children[1])
        else:
            return
