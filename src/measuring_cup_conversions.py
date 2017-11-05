# 1 Cup = 16 Tablespoons
# 1 Tablespoon = 3 Teaspoons
# 1 Cup = 48 Teaspoons
class MeasuringCupConversions():
    def from_cups_get_measure(self, number, unit):
        if unit == "cup":
            return "%i cups" % number
        if unit == "tablespoons" and number % 16:
            return "%i cups" % number / 16
        if unit == "tablespoons" and not(number % 16) and number > 16:
            num_of_cups = number / 16
            number = number % 16
            return "%i cups and %i tablespoons" % (num_of_cups, number)
        if unit == "tablespoons" and not(number % 16) and number < 16:
            return "%i tablespoons" % number
        if unit == "teaspoons" and number % 3 == 0 and number < 48:
            return "%i tablespoons" % (number / 3)
        if unit == "teaspoons" and number % 3 == 0 and not(number % 48 == 0) and number > 48:
            return "%i tablespoons" % (number / 3)
        if unit == "teaspoons" and number % 48 == 0:
            return "%i cups" % (number / 48)
        if unit == "teaspoons" and not(number % 3 == 0) and number > 48:
            num_of_cups = number / 48
            number = number % 48
            num_of_tablespoons = number / 3
            number = number % 3
            return "%i cups, %i tablespoons, %i teaspoons" % (num_of_cups, num_of_tablespoons, number)
        if unit == "teaspoons" and not(number % 3 == 0) and 2 < number < 48:
            num_of_tablespoons = number / 3
            number = number % 3
            return "%i tablespoons and %i teaspoons" % (num_of_tablespoons, number)
        else:
            return "%i teaspoons" % (number)

number = int(raw_input("Enter number: "))
unit = raw_input("Enter unit: ")
GivenNumberAndUnit = MeasuringCupConversions()
print GivenNumberAndUnit.from_cups_get_measure(number, unit)
