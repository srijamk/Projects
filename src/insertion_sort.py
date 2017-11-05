import sys
import time

class InsertionSort():
  def insertion_sort(self, lst):
    # staring with 1, as value at lst[0] is already sorted
    for i in range(1, len(lst)):
      # our marker
      j = i
      # make a copy of value at the marker
      temp = lst[j]
      # marker should be greater than 0 and marker value should be less than predecessor value
      while j >= 1 and temp < lst[j-1]:
        # swap the value at marker with value at predecessor
        lst[j] = lst[j-1]
        lst[j-1] = temp
        # continue until marker value is greater than its predecessor
        j -= 1
    return lst

if __name__ == '__main__':
  if len(sys.argv) != 2:
    lst = raw_input("Enter one list: ").split(", ")
  else:
    lst = sys.argv[1]

  insertion = InsertionSort()
  print insertion.insertion_sort(lst)
