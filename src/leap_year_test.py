import unittest
from leap_year import LeapYear


class TestLeapYear(unittest.TestCase):
    def test_leap_year(self):
      year = LeapYear()
      self.assertTrue(year.is_leap_year(2004))
      self.assertFalse(year.is_leap_year(1900))
      self.assertTrue(year.is_leap_year(400))
      self.assertTrue(year.is_leap_year(2000))
      self.assertFalse(year.is_leap_year(-1))

if __name__ == '__main__':
  unittest.main()
