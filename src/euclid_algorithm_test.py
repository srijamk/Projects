import unittest
from euclid_algorithm import EuclidAlgorithm

class TestEuclidAlgorithm(unittest.TestCase):
  def test_gcd(self):
    numbers = EuclidAlgorithm()
    self.assertEqual(2, numbers._gcd(2, 4))
    self.assertEqual(1, numbers._gcd(16, 23))

if __name__ == '__main__':
  unittest.main()
