import unittest
from in_order import Order

class TestOrder(unittest.TestCase):
  def test_order(self):
    numbers = Order()
    self.assertEqual([1], numbers.order([1]))
    self.assertEqual([1, 2], numbers.order([2, 1]))
    self.assertEqual([1, 2, 3, 3, 5, 7], numbers.order([2, 3, 1, 5, 3, 7]))

if __name__ == '__main__':
  unittest.main()
