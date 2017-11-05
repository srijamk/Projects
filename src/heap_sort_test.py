import unittest
from heap_sort import HeapSort

class TestHeapSort(unittest.TestCase):
  def test_heap_sort(self):
    lst = HeapSort()
    self.assertEqual([1, 2, 3], lst.heap_sort([2, 1, 3]))

if __name__ == '__main__':
  unittest.main()
