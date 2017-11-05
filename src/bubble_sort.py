import sys

class BubbleSort():
    def sort(self, lst):
      for i in range(len(lst)):
        for k in range(len(lst) - 1, i, -1):
          if lst[k] < lst[k - 1]:
            lst[k], lst[k - 1] = lst[k - 1], lst[k]
      return lst

if __name__ == '__main__':
  if len(sys.argv) != 2:
    lst = raw_input("Enter a valid list of numbers: ").split(", ")
  else:
    lst = sys.argv[1]
  bubble = BubbleSort()
  print bubble.sort(lst)
