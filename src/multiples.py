import sys

class Multiples:
  def multiples(self, a, b):
    return a % b == 0 or b % a == 0

if __name__ == '__main__':

  if len(sys.argv) != 3:
    a, b = raw_input("Enter two numbers: ").split( )
  else:
    a = sys.argv[1]
    b = sys.argv[2]

  numbers = Multiples()
  print numbers.multiples(int(a), int(b))
