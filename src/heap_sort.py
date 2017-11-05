import sys
import time

class HeapSort():
  def heap_sort(self, lst):
    start = time.time()
    sorted_list = []
    index = -1
    for i in range(len(lst)):
      sorted_list.append("num")
    while len(lst) >= 1:
      while index >= (-1) - len(lst):
        sorted_list[index] = max(lst)
        lst.remove(max(lst))
        index -= 1
    end = time.time()
    elapsed = end - start
    return "Time: " + str(elapsed)


if __name__ == '__main__':
  if len(sys.argv) != 2:
    lst = raw_input("Enter one list: ").split(", ")
  else:
    lst = sys.argv[1]
  num = HeapSort()
  print num.heap_sort(lst)
