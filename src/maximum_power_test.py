import unittest
from maximum_power import MaximumPower

class TestMaximumPower(unittest.TestCase):
  def test_maximum_power(self):
    number = MaximumPower()
    self.assertEqual(5, number.maximum_power(34))
    self.assertEqual(6, number.maximum_power(67))

if __name__ == '__main__':
  unittest.main()
