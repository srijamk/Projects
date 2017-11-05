import unittest
from median_of_five import MedianOfFive

class TestMedianOfFive(unittest.TestCase):
  def test_median_of_five(self):
    num = MedianOfFive()
    self.assertEqual(3, num.median(1, 2, 3, 4, 5))
    self.assertEqual(19, num.median(1, 9, 19, 20, 100))

if __name__ == '__main__':
  unittest.main()
