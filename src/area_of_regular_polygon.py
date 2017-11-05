import math

class Area():
    def get_area_of_regular_polygon(self, s, n):
        return "Area is %.2f." % ((n * s**2) / (4 * math.tan((math.pi) / n)))

s = int(input("Enter length of sides: "))
n = int(input("Enter number of sides: "))
measurements = Area()
print measurements.get_area_of_regular_polygon(s, n)
