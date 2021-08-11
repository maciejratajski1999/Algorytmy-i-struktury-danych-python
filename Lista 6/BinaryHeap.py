class BinaryHeap:

    def __init__(self, elements=[]):
        self.elements = []
        for element in elements:
            self.insert(element)

    def __str__(self):
        return str(self.elements)

    def insert(self, new_element):
        self.elements.append(new_element)
        index = len(self.elements) - 1
        parent_index = int((index-1)/2)
        while self.elements[index] < self.elements[parent_index]:
            self.elements[index], self.elements[parent_index] = self.elements[parent_index], self.elements[index]
            index = parent_index
            parent_index = int((index-1)/ 2)

    def pop(self):
        if len(self.elements) == 1:
            return self.elements.pop()
        elif self.elements == []:
            return None
        first_value = self.elements[0]
        last_value = self.elements.pop()
        self.elements[0] = last_value
        index = 0
        while index*2 < len(self.elements)-1:
            left = index*2 + 1
            right = index*2 + 2
            if right >= len(self.elements):
                selected = left
            else:
                if self.elements[left] <= self.elements[right]:
                    selected = left
                else:
                    selected = right
            if self.elements[index] <= self.elements[selected]:
                break
            else:
                self.elements[index], self.elements[selected] = self.elements[selected], self.elements[index]
                index = selected
        return first_value

    def sort(self):
        sorted_list = []
        for i in range(0,len(self.elements)):
            sorted_list.append(self.pop())
        self.elements = sorted_list
        return sorted_list




