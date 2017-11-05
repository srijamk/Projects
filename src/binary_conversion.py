import sys

class Binary():
  def binary(self, n):
    string = ""
    v = 1
    while v < n:
        # doubles v
        v = v * 2
    while v > 0:
        if n < v:
            # if the sum of the powers of 2 is not the maximum, add a 0
            string += "0"
        else:
            # if the given power of 2 is the maximum value to get to n, add a 1
            string += "1"
            n -= v
            v = v / 2

    return string

if __name__ == '__main__':
    if len(sys.argv) != 2:
        n =  raw_input("Please enter a valid number: ")
    else:
        n = sys.argv[1]

    get = Binary()
    print get.binary(int(n))
