class Multiplication():
    def get_table(self):
        row = ""
        for a in range(1, 11):
            for b in range(1, 11):
                row += "\t" + str(a * b)
                if b == 10:
                    row += "\n"
        print row

GivenNumbers = Multiplication()
print GivenNumbers.get_table()
