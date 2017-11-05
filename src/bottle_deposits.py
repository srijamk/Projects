# This program returns the refund on different-sized bottles.

class Refund():
    LITER_OR_LESS = .1
    MORE_THAN_ONE_LITER = .25
    def bottle_deposit(self, small, big):
        return "Your refund is $%.2f" % float(self.LITER_OR_LESS * small + self.MORE_THAN_ONE_LITER * big)

small = int(input("Enter the number of small bottles: "))
big = int(input("Enter the number of big bottles: "))

calculate = Refund()
print calculate.bottle_deposit(small, big)
