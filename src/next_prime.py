import sys
from is_prime import IsPrime
class Prime():
    def get_next_prime(self, num):
        while True:
            num += 1
            if IsPrime().is_prime(num):
                return num

    def main(self):
        num = int(raw_input("Enter a number: "))
        print "Next prime is %i. " % Prime().get_next_prime(num)

if __name__ == '__main__':
    Prime().main()
