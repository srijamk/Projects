import sys

class IsPrime():
    def is_prime(self, num):
        prime = True
        for x in range(2, num / 2 + 1):
            if num % x == 0:
                prime = False
        if num == 1:
            prime = False

        return prime

if __name__ == '__main__':
    if len(sys.argv) != 2:
        num = int(raw_input("Enter a number: "))
    print IsPrime().is_prime(num)
