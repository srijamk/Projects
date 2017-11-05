import unittest
from star_matrix import StarMatrix

class TestStarMatrix(unittest.TestCase):
  def test_star_matrix(self):
    N = StarMatrix()
    self.assertEqual("*", N.star_matrix(1))
    self.assertEqual("**\n**", N.star_matrix(2))
    self.assertEqual("***\n***\n***", N.star_matrix(3))

if __name__ == '__main__':
  unittest.main()
