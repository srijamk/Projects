class EvenOrOdd():
    def get_even_or_odd(self, number):
        return number % 2 == 0

number = int(input("Enter a number: "))
Number = EvenOrOdd()
if Number.get_even_or_odd(number) == True:
    print "Even!"
else:
    print "Odd!"
