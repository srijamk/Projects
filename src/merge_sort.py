import sys

class MergeSort():
  def _sort(self, lst):
    return self.sort(lst, 0, len(lst))

  def sort(self, lst, low, high):
    length = high - low
    if length <= 1:
      return
    mid = low + length / 2
    self.sort(lst, low, mid)
    self.sort(lst, mid, high)
    temp = range(0, length)
    i = low
    j = mid
    for k in range(0, length):
      current_val = 0
      if i == mid:
        current_val = lst[j]
        j += 1
      elif j == high:
        current_val = lst[i]
        i += 1
      elif lst[j] < lst[i]:
        current_val = lst[j]
        j += 1
      else:
        current_val = lst[i]
        i += 1
      temp[k] = current_val

    for k in range(0, length):
      lst[low + k] = temp[k]

    return lst

if __name__ == '__main__':
  if len(sys.argv) != 2:
    lst = raw_input("Enter a valid list of numbers: ").split(" ")
  else:
    lst = sys.argv[1]
  merge = MergeSort()
  print merge._sort(lst)
