import sys

class MedianOfFive:
  def median(self, num1, num2, num3, num4, num5):
    """
    Returns median given five parameters in no given order. I remove the min and
    the max of the numbers twice so I am left with the middle value, the median.
    """
    num_list = [num1, num2, num3, num4, num5]
    for x in range(2):
      num_list.remove(max(num_list))
      num_list.remove(min(num_list))
    return num_list[0]

if __name__ == '__main__':
  if len(sys.argv) != 6:
    num1, num2, num3, num4, num5 = raw_input("Enter five numbers in no specific order: ").split( )
  else:
    num1 = sys.argv[1]
    num2 = sys.argv[2]
    num3 = sys.argv[3]
    num4 = sys.argv[4]
    num5 = sys.argv[5]


  numbers = MedianOfFive()
  print "The median of " + num1 + ", " + num2 + ", " + num3 + ", " + num4 + ", and " + num5 + " is " + str(numbers.median(int(num1), int(num2), int(num3), int(num4), int(num5))) + "."
