import math

class Arithmetic():
    def arithmetics(self, a, b):
        return "\na + b = %.2f\na - b = %.2f\na * b = %.2f\na / b = %.3f\na %% " "b = %.1f\nlog10 a = %.2f\na^b is %.2f\n" % (a + b, a - b, a * b, float(a) / float(b), float(a) % float(b), math.log10(a), a ** b)

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

calculate = Arithmetic()
print calculate.arithmetics(a, b)
