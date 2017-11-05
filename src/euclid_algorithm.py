import sys

class EuclidAlgorithm():
  def _gcd(self, x, y):
    gcd = 0
    if x % y == 0 or y % x == 0:
      gcd = min(x, y)
    else:
      if x % ((x - y) % y) == 0:
        gcd = (x - y) % y

    return gcd

if __name__ == '__main__':
  if len(sys.argv) != 3:
    x, y = raw_input("Enter two numbers: ").split( )
  else:
    x = sys.argv[1]
    y = sys.argv[2]

  numbers = EuclidAlgorithm()
  print numbers._gcd(int(x), int(y))
