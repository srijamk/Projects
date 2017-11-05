import unittest
from multiples import Multiples

class TestMultiples(unittest.TestCase):
  def test_multiples(self):
    numbers = Multiples()
    self.assertTrue(numbers.multiples(2, 4))
    self.assertFalse(numbers.multiples(2, 5))

if __name__ == '__main__':
  unittest.main()
