import unittest
from merge_sort import MergeSort

class TestMergeSort(unittest.TestCase):
  def test_merge_sort(self):
    lst = MergeSort()
    self.assertEqual([1, 2], lst.merge_sort([2, 1]))

if __name__ == '__main__':
  unittest.main()
