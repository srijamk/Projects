import sys

class Physics:
  def displacement(self, x0, v0, t):
    return x0 + v0 * t + (9.78033) * (t ** 2) / 2

if __name__ == '__main__':

  if len(sys.argv) != 4:
    x0, v0, t = raw_input("Enter three values respectively - Initial Position, Velocity, Seconds: ").split( )

  else:
    x0 = sys.argv[1]
    v0 = sys.argv[2]
    t = sys.argv[3]

  object = Physics()
  print object.displacement(int(x0), int(v0), int(t))
