import unittest
from wind_chill import WindChill

class TestWindChill(unittest.TestCase):
  def test_wind_chill(self):
    wind = WindChill()
    self.assertEqual(1.039, wind.wind_chill(1, 1))

if __name__ == '__main__':
  unittest.main()
