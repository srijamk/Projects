import unittest
from newton_square_root import NewtonSquareRoot

class Test_Square_Root(unittest.TestCase):
  def test_square_root(self):
    square = NewtonSquareRoot()
    self.assertEqual(3, square.square_root(9))
    self.assertEqual(2, square.square_root(4))

if __name__ == '__main__':
  unittest.main()
