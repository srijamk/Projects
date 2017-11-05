import sys
def add(x, y):
    return "Sum: %i" % (x + y)
    
if __name__ == '__main__':
  if len(sys.argv) != 2:
    num = raw_input("Enter one number: ")
    num2 = raw_input("Enter another number: ")
  else:
    num = sys.argv[1]
    num2 = sys.argv[2]

  print add(int(num), int(num2))
