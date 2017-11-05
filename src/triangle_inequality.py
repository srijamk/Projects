import sys

class Triangle:
  def inequality(self, a, b, c):
    """
    Tests whether one side length is less than the sum of the other two side lengths.
    """
    return a < b + c and b < a + c and c < b + a

if __name__ == '__main__':

  if len(sys.argv) != 4:
    a, b, c = raw_input("Enter 3 values: ").split( )
  else:
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]

  triangle = Triangle()
  print triangle.inequality(int(a), int(b), int(c))
