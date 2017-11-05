class Duplicates():
    def has_duplicates(self, string):
        ascii_list = [False] * 127
        for char in string:
            index = ord(char)
            if not (ascii_list[index]):
                ascii_list[index] = True
            else:
                return True
        return False

string = "the"
print Duplicates().has_duplicates(string)
