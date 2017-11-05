import unittest
from triangle_inequality import Triangle

class TestTriangle(unittest.TestCase):
  def test_inequality(self):
    triangle = Triangle()
    self.assertTrue(triangle.inequality(3, 10, 9))
    self.assertFalse(triangle.inequality(2, 9, 7))

if __name__ == '__main__':
  unittest.main()
