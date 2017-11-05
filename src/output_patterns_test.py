import unittest
from output_patterns import OutputPatterns

class TestOutputPatterns(unittest.TestCase):
    def test_right_triangle(self):
      triangle = OutputPatterns()
      self.assertEqual("**\n*\n", triangle.right_triangle(2))

if __name__ == '__main__':
    unittest.main()
