import unittest
from harmonic_numbers import HarmonicNumbers

class TestHarmonicNumbers(unittest.TestCase):
  def test_harmonic_numbers(self):
    num = HarmonicNumbers()
    self.assertEqual(1.83, num.harmonic_numbers(3))
    self.assertEqual(2.08, num.harmonic_numbers(4))
    self.assertEqual(2.45, num.harmonic_numbers(6))

if __name__ == '__main__':
  unittest.main()
