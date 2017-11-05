import unittest
from sine import Sine

class TestSine(unittest.TestCase):
  def test_calculate_sine(self):
    t = Sine()
    self.assertEqual(1.05, t.calculate_sine(1))

if __name__ == '__main__':
  unittest.main()
