import unittest
from ascending_or_descending import AscendingOrDescending

class TestAscendingOrDescending(unittest.TestCase):
  def test_are_in_order(self):
    numbers = AscendingOrDescending()
    self.assertTrue(numbers.are_in_order(1, 2, 3))
    self.assertFalse(numbers.are_in_order(2, 5, 3))

if __name__ == '__main__':
  unittest.main()
