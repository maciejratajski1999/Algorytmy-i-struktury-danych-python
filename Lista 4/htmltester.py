from stack import Stack

#zadanie 4
class HTMLTester:

    def __init__(self, path):
        self.path = path
        self.file = open(self.path).read()

    def read_next_token(self):
        '''
        :return: ("tag", if closing tag return True)
                if the file ends, return None
                if the tag is closing in itself like <tag /> return "closed"
        '''
        if self.file == "":
            return None
        if self.file[0] == "<":
            tag = ""
            self.file = self.file[1:]
            tag_type = self.file[0] == "/"
            if tag_type:
                self.file = self.file[1:]
            while self.file[0] in {" ", "\n"}:
                self.file = self.file[1:]
            while self.file[0] not in {" ", ">", "\n"}:
                tag = tag + self.file[0]
                self.file = self.file[1:]
            while self.file[0] not in {"/", ">"}:
                self.file = self.file[1:]
            if self.file[0] == "/":
                if self.file[1] == ">":
                    return "closed"
            return tag, tag_type
        else:
            self.file = self.file[1:]
            return self.read_next_token()

    def parse(self):
        '''
        :return: True if the HTML code has valid tags
                or raise ValueError if not
        '''
        tags = Stack()
        in_progress = True
        while in_progress:
            next_tag = self.read_next_token()
            if next_tag == None:
                if not tags.isEmpty():
                    raise ValueError("leftover tags with no closing: " + str(tags))
            elif next_tag == "closed":
                continue
            elif next_tag[1]:
                if next_tag[0] != tags.pop():
                    raise ValueError("closing tag out of place: /" + next_tag[0])
            else:
                tags.push(next_tag[0])
            in_progress = next_tag != None
        return True

# print(HTMLTester("sample.html").parse())
# print(HTMLTester("sample2.html").parse())
# print(HTMLTester("sample3.html").parse())


