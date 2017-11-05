import unittest
from sideways_triangle_two import SidewaysTriangle

class SidewaysTriangleTest(unittest.TestCase):
    def sideways_triangle_two_test(self):
      triangle = SidewaysTriangle()
      self.assertEqual("*\n**\n", triangle.sideways_triangle_two(2))

if __name__ == '__main__':
    unittest.main()
