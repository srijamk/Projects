import sys

class PowersOfTwo:
  def _print(self, n):
    title_row = ["P", "V"]
    row_list = []
    value = 2 ** n
    second_row = "|  " + str(n) + "   |     " + str(value) + "|"

    for i in range(n):
      row_list.append("|  " + str(i) + "   |     " + str(2 ** i) + "|")
    row_list.append(second_row)


    print "|Power | Value|"
    for row in row_list:
      print row

if __name__ == '__main__':
  if len(sys.argv) != 2:
    n = raw_input("Enter one number to get the value of 2 to the power of the number: ").split( )
  else:
    n = sys.argv[1]

  number = PowersOfTwo()
  print number._print(int(n))
