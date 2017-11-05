class Triangle():
    def get_validity(self, side1, side2, side3):
        minimum = min(side1, side2, side3)
        maximum = max(side1, side2, side3)
        median = (side1 + side2 + side3) - minimum - maximum
        return  median - minimum < maximum < median + minimum

side1 = int(raw_input("Enter a triangle side: "))
side2 = int(raw_input("Enter another triangle side: "))
side3 = int(raw_input("Enter another triangle side: "))
GivenSides = Triangle()
print GivenSides.get_validity(side1, side2, side3)
