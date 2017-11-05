import sys
import math

class Sine:
  def calculate_sine(self, t):
    return round(math.sin(2 * t) + math.sin(3 * t), 2)

if __name__ == '__main__':
  if len(sys.argv) != 2:
    t = raw_input("Enter one number: ")
  else:
    t = sys.argv[1]

  num = Sine()
  print num.calculate_sine(float(t))
