class Ruler:
  def print_num(self, num):
    """
    Returns relative distance of notches on a ruler.
    """
    result = ""
    x = 1


    while x <= num:
      # When x is 1, it represents the smallest line on the ruler.
      # As x increases, the taller the lines on the ruler become.
      result = result + str(x) + result
      x += 1
    return result

_ruler = Ruler()
print (_ruler.print_num(3))
