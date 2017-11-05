import sys

class MaximumPower:
  def maximum_power(self, n):
    power_list = []
    i = 0
    while n >= 2 ** i:
      power_list.append(i)
      i += 1
    return max(power_list)

if __name__ == '__main__':
  if len(sys.argv) != 2:
    n = raw_input("Enter only one number: ").split( )
  else:
    n = sys.argv[1]

  number = MaximumPower()
  print number.maximum_power(int(n))
