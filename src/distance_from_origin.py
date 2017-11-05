import math
import sys

class DistanceFromOrigin():
    def get_distance(self, x, y):
        return math.sqrt((x**2) + (y**2))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        x, y = raw_input("Please type two valid numbers: ").split( )
    else:
        x = sys.argv[1]
        y = sys.argv[2]

    numbers = DistanceFromOrigin()
    print numbers.get_distance(int(x), int(y))
