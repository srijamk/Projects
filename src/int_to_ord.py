import sys

class Convert():
    int_to_ord = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth",
    7: "seventh",
    8: "eighth",
    9: "ninth",
    10: "tenth",
    11: "eleventh",
    12: "twelfth"
    }
    def get_ord(self, number):
        if number in self.int_to_ord.keys():
            return self.int_to_ord[number]
        else:
            return ""

if __name__ == '__main__':
    if len(sys.argv) != 2:
        number = int(raw_input("Enter a number: "))
    else:
        number = sys.argv[1]
    GivenNumber = Convert()
    print GivenNumber.get_ord(number)
