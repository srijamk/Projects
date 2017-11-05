import unittest
from selection_sort import SelectionSort

class TestSelectionSort(unittest.TestCase):
  def test_selection_sort(self):
    lst = SelectionSort()
    self.assertEqual([1, 1, 2, 3, 5, 6, 7, 8, 9], lst.selection_sort([6, 3, 5, 1, 8, 2, 7, 1, 9]))

if __name__ == '__main__':
  unittest.main()
