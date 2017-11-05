import unittest
from spring_months import SpringMonths

class TestSpringMonths(unittest.TestCase):
  def test_spring_months(self):
    date = SpringMonths()
    self.assertTrue(date.is_in_spring(4, 21))
    self.assertFalse(date.is_in_spring(12, 20))

if __name__ == '__main__':
  unittest.main()
