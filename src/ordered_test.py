import unittest
from ordered import Order

class TestOrde(unittest.TestCase):
  def test_in_order(self):
    numbers = Order()
    self.assertEqual([1, 2, 3], numbers.in_order(3, 1, 2))

if __name__ == '__main__':
  unittest.main()
