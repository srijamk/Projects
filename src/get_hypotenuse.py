import math

class Triangle():
    def get_hypotenuse(self, a, b):
        return math.sqrt(a ** 2 + b ** 2)

a = int(raw_input("Enter an a value: "))
b = int(raw_input("Enter a b value: "))
GivenSides = Triangle()
print GivenSides.get_hypotenuse(a, b)
