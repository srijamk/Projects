import sys

class 




if __name__ == '__main__':
  if len(sys.argv) != 2:
    num = raw_input("Enter a valid number: ")
  else:
    num = sys.argv[1]
  number = PrimeFactors()
  print number.primes(int(num))
