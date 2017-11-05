from proper_divisors import ProperDivisors
class PerfectNumbers():
    def is_perfect(self, number):
        if number == sum(ProperDivisors().get_proper_divisors(number)):
            print str(number) + " is Perfect"
        else:
            print str(number) + " is not Perfect"

number = int(raw_input("Enter a number: "))
print PerfectNumbers().is_perfect()
