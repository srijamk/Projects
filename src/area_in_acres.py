# This program prints a field's area in acres given length and width in feet.

class Area():
    SQFT_PER_ACRE = 43560
    def feet_to_acres(self, length, width):
        area_in_feet = length * width
        return area_in_feet / self.SQFT_PER_ACRE


length = float(input("Enter length of field: "))
width = float(input("Enter width of field: "))

Feet = Area()
print Feet.feet_to_acres(length, width)
