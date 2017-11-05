class NameThatShape():
    def get_shape(self, number_of_sides):
        gon_strings = ["penta", "hexa", "hepta", "octa", "nona", "deca"]
        if number_of_sides == 3:
            return "Triangle"
        elif number_of_sides == 4:
            return "Square"
        else:
            return gon_strings[number_of_sides - 5] + "gon"

number_of_sides = int(input("Enter a number of sides: "))
Number = NameThatShape()
print Number.get_shape(number_of_sides)
