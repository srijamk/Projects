class Numbers():
    def number_file(self, file, another_file):
        f_lines = []
        f = open(file, 'r')
        new_file = open(another_file, 'w')
        count_lines = len(f.readlines())
        f = open(file, 'r')
        for line in f:
            f_lines.append(str(line))
        x = 1
        while x <= count_lines:
            new_file.write(str(x) + ": " + f_lines[x - 1])
            x += 1

print Numbers().number_file("average.py", "new_file.py")
