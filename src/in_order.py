import sys
import ast

class Order:
  def order(self, r):
    if r[0] > r[1]:
      print "The first number is bigger than the second number."
    elif r[0] > r[2]:
      print "The first number is bigger than the third number."
    elif r[1] > r[2]:
      print "The second number is bigger than the third number."
    else:
      print "The numbers are in order."

if __name__ == '__main__':
  if len(sys.argv) != 2:
    lst = raw_input("Please enter ONE list: ").split(', ')
  else:
    lst = sys.argv[1]

  num = Order()
  print num.order(lst)
