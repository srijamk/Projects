import unittest
from prime_counter import PrimeCounter

class TestPrimeCounter(unittest.TestCase):
  def test_prime_counter(self):
    number = PrimeCounter()
    self.assertEqual(8, number.get_primes(20))

if __name__ == '__main__':
  unittest.main()
