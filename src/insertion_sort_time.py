import sys
import random
import time
from quick_sort import QuickSort
from measure_time import MeasureTime


if __name__ == '__main__':
  if len(sys.argv) != 3:
    trials, n = raw_input("Enter a valid number of trials and a valid number n: ").split( )
  else:
    trials = sys.argv[1]
    n = sys.argv[2]
  measuretime = MeasureTime()


  print measuretime.measure(int(trials), int(n), QuickSort())
