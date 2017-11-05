class FuelEfficiency():
    def us_to_canada(self, mpg):
        return str(mpg) + " in l/100km is " + str(235.214583 / mpg) + "."

mpg = float(input("Enter an amount in miles per gallon: "))
calculate = FuelEfficiency()
print calculate.us_to_canada(mpg)
