class Integer():
    def is_integer(self, string):
        is_integer = True
        for char in string:
            if not(32 < ord(char) <= 57):
                is_integer = False
        return is_integer

    def main(self):
        string = raw_input("Enter a string: ")
        GivenString = Integer()
        if GivenString.is_integer(string):
            print "The string represents an integer."
        else:
            print "The string does not represent an integer."

if __name__ == '__main__':
    Integer().main()
