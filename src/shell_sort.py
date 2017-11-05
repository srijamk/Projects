import sys
from insertion_sort import InsertionSort

class ShellSort():
  def shell_sort(self, lst):
    h = len(lst) / 2

    while h > 0:
      for i in range(len(lst)):
        j = i
        swap = lst[i]
        while j >= h and lst[j - h] > swap:
          lst[j] = lst[j - h]
          j -= h
        lst[j] = swap
      h = h / 2
    return lst

if __name__ == '__main__':
  if len(sys.argv) != 2:
    lst = raw_input("Enter a valid list of numbers: ").split(", ")
  else:
    lst = sys.argv[1]
  shell = ShellSort()
  print shell.shell_sort(lst)
