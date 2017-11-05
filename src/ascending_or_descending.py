import sys

class AscendingOrDescending:
  def are_in_order(self, x, y, z):
    return x < y < z or x > y > z

if __name__ == '__main__':

  if len(sys.argv) != 4:
    x, y, z = raw_input("Enter four numbers: ").split( )

  else:
    x = sys.argv[1]
    y = sys.argv[2]
    z = sys.argv[3]

  numbers = AscendingOrDescending()
  print numbers.are_in_order(x, y, z)
