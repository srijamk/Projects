import unittest
from numbers_are_equal import EqualNumbers

class TestEqualNumbers(unittest.TestCase):
  def test_are_equal(self):
    numbers = EqualNumbers()
    self.assertEqual(True, numbers.are_equal(1, 1, 1))
    self.assertEqual(False, numbers.are_equal(2, 5, 4))

if __name__ == '__main__':
  unittest.main()
