import unittest
from color_conversion import ColorConversion

class TestColorConversion(unittest.TestCase):
  def test_color_conversion(self):
    rgb = ColorConversion()
    self.assertEqual([0, 0, 0, 1], rgb.cmyk_conversion(0, 0, 0))

if __name__ == '__main__':
  unittest.main()
