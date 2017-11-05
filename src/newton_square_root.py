import sys


class NewtonSquareRoot():
  def square_root(self, num):
    guess = 1
    while abs(guess - (num / guess)) > (1e-18 * guess):
      guess = ((num / guess) + guess) / 2.0

    return guess

if __name__ == '__main__':
  if len(sys.argv) != 2:
    num = raw_input("Enter one number: ")
  else:
    num = sys.argv[1]

  number = NewtonSquareRoot()
  print number.square_root(int(num))
