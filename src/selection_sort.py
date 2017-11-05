import sys

class SelectionSort():
  def sort(self, lst):
    for item in lst:
      item = int(item)

    # loops through every item in the list
    for i in range(len(lst)):
      # makes a copy of i
      k = i
      # creates the marker
      for j in range(i + 1, len(lst)):
        # compares marker value with its predecessors
        if lst[j] < lst[k]:
          # swaps the values
          k = j
          self.swap(lst, i, k)


    return lst

  def swap(self, lst, a, b):
    temp = lst[a]
    lst[a] = lst[b]
    lst[b] = temp

if __name__ == '__main__':
  if len(sys.argv) != 2:
    lst = raw_input("Enter a valid list of numbers: ").split(", ")
  else:
    lst = sys.argv[1]
  selection = SelectionSort()
  print selection.sort(lst)
