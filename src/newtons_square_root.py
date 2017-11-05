class SquareRoot():
    def get_square_root(self, x):
        guess = x / 2
        while abs(x - guess ** 2) >= 10**-12:
            guess = (guess + (x / guess)) / 2.0
            print guess
        return guess
x = int(raw_input("Enter a number: "))
GivenNumber = SquareRoot()
print GivenNumber.get_square_root(x)
