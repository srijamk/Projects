class NameThatTriangle():
    def get_triangle_type(self, side1, side2, side3):
        if side1 == side2 == side3:
            return "Equilateral"
        elif side1 != side2 and side2 != side3:
            return "Scalene"
        else:
            return "Isosceles"
side1 = int(input("Enter length of Side 1: "))
side2 = int(input("Enter length of Side 2: "))
side3 = int(input("Enter length of Side 3: "))
given_side_lengths = NameThatTriangle()
print given_side_lengths.get_triangle_type(side1, side2, side3)
