import os.path

class Head():
    def display_head(self, file):
        f_lines = []
        line_counter = 0
        f = open(file, 'r')
        for line in f:
            f_lines.append(str(line))
        while line_counter < 10:
            print f_lines[line_counter]
            line_counter += 1

    def display_tail(self, file):
        f_lines = []
        line_counter = -10
        f = open(file, 'r')
        for line in f:
            f_lines.append(str(line))
        while line_counter <= -1:
            print f_lines[line_counter]
            line_counter += 1

file = raw_input("Enter a file name: ")
if os.path.isfile(file):
    print Head().display_tail(file)
else:
    print "Sorry, invalid file."
