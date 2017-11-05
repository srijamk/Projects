import sys

class SquareRoot():
  def square_root(self, num):
    guess = 1
    if guess * guess == num:
      return guess
    else:
      for x in range(1000):
        guess = (guess + (num / guess)) / 2.0
    return guess

if __name__ == '__main__':
  if len(sys.argv) != 2:
    num = raw_input("Enter one number: ")
  else:
    num = sys.argv[1]

  number = SquareRoot()
  print number.square_root(int(num))
