import sys

class SpringMonths:
  def is_in_spring(self, m, d):
    if m == 3:
      return 20 <= d <= 31
    elif m == 6:
      return 1 <= d <= 20
    else:
      return 3 < m < 6

if __name__ == '__main__':

  if len(sys.argv) != 3:
    m, d = raw_input("Enter two numbers respectively - Month, Day: ").split( )

  else:
    m = sys.argv[1]
    d = sys.argv[2]

  date = SpringMonths()
  print date.is_in_spring(m, d)
