import sys

class SumOfAllValues():
  def sum_of_all_values(self, n):
    sum = 0
    for i in range(n + 1):
      sum += i
    return sum

if __name__ == '__main__':
  if len(sys.argv) != 2:
    n = raw_input("Enter one number: ").split( )
  else:
    n = sys.argv[1]

  num = SumOfAllValues()
  print num.sum_of_all_values(int(n))
