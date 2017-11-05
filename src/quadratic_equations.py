import math

class QuadraticEquations():
    def get_number_of_solutions(self, a, b, c):
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            return "No real roots"
        elif discriminant == 0:
            return "One real root"
        else:
            return "Two real roots"

    def get_roots(self, a, b, c):
        first_root = (-b + math.sqrt(b**2 - 4*a*c)) / 2*a
        second_root = (-b - math.sqrt(b**2 - 4*a*c)) / 2*a
        if first_root == second_root:
            return first_root
        else:
            return first_root, second_root

a = int(input("Enter value a in equation ax^2 + bx + c: "))
b = int(input("Enter value b in equation ax^2 + bx + c: "))
c = int(input("Enter value c in equation ax^2 + bx + c: "))
givenValues = QuadraticEquations()
print givenValues.get_number_of_solutions(a, b, c)
print givenValues.get_roots(a, b, c)
