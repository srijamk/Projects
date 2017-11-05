import unittest
from sum_all_values import SumOfAllValues

class TestSumOfAllValues(unittest.TestCase):

  @staticmethod
  def sum(n):
    return (n * (n + 1)) / 2

  def test_sum_of_all_values(self):
    n = SumOfAllValues()
    self.assertEqual(TestSumOfAllValues.sum(1), n.sum_of_all_values(1))
    self.assertEqual(TestSumOfAllValues.sum(2), n.sum_of_all_values(2))

if __name__ == '__main__':
  unittest.main()
