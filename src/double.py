import sys

def double(x):
    return "Double: %i" % (x * 2)
    
if __name__ == '__main__':
  if len(sys.argv) != 2:
    num = raw_input("Enter one number: ")
  else:
    num = sys.argv[1]

  print double(int(num))
