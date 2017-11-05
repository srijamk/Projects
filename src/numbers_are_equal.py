import sys

class EqualNumbers:
  def are_equal(self, a, b, c):
    return a == b == c

if __name__ == '__main__':
  if len(sys.argv) != 4:
    a, b, c = raw_input("Enter three numbers in no specific order: ").split( )
  else:
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]

  numbers = EqualNumbers()
  print numbers.are_equal(a, b, c)
