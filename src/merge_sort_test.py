import unittest
from merge_sort import MergeSort

class TestMergeSort(unittest.TestCase):
  def test_merge_sort(self):
    lst = MergeSort()
    self.assertEqual([1, 1, 2, 3, 4, 5, 6, 7], lst.middle_sort([2, 1, 3, 1, 7, 4, 5, 6]))

if __name__ == '__main__':
  unittest.main()
