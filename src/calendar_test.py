import unittest
from calendar import Calendar

class TestCalendar(unittest.TestCase):
  def test_day_of_the_week(self):
    cal = Calendar()
    self.assertEqual("Monday", cal.day_of_the_week(2, 14, 2000))
    self.assertEqual("Friday", cal.day_of_the_week(7, 4, 2014))

if __name__ == '__main__':
  unittest.main()
