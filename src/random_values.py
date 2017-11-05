import sys
import random

class RandomValues:
  def random_values(self, n):
    n_list = []
    for i in range(n):
      n_list.append(random.random())
    average_value = sum(n_list) / n
    return str(n_list) + ", " + str(average_value)

if __name__ == '__main__':
  if len(sys.argv) != 2:
    n = raw_input("Enter one number: ").split( )
  else:
    n = sys.argv[1]

  number = RandomValues()
  print number.random_values(int(n))
