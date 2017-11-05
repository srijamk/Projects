import sys

class Order:
  def in_order(self, a, b, c):
    mi = min(a, b, c)
    ma = max(a, b, c)
    mid = c
    if(a != mi and a != ma):
      mid = a
    elif (b != mi and b != ma):
      mid = b
      
    return [mi, mid, ma]

if __name__ == '__main__':
  if len(sys.argv) != 4:
    a, b, c = raw_input("Enter three numbers in no specific order: ").split( )
  else:
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]


  numbers = Order()
  print numbers.in_order(int(a), int(b), int(c))
