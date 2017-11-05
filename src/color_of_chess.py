import sys

class ColorOfSquare():

    def isEven(self, number):
        return number % 2 == 0

    def get_color(self, position):
        col = ord(position[0]) - 96
        row = ord(position[1]) - 48

        if len(position) != 2 or not (0 < col < 9) or not (0 < row < 9):
            return "Unknown"

        if self.isEven(col) and self.isEven(row)\
        or not self.isEven(col) and not self.isEven(row):
            return "Black"
        else:
            return "White"

position = raw_input("Enter a position-letter then number: ")
given_position = ColorOfSquare()
while len(position) > 0:
    print given_position.get_color(position)
    position = raw_input("Enter a position-letter then number: ")
