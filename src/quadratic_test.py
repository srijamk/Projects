import unittest
from quadratic import Quadratic

class TestQuadraticSolver(unittest.TestCase):
    def test_quadratic(self):
      _quadratic = Quadratic()
      self.assertEqual((-2.0, -1.0), _quadratic.solve(3, 2))

if __name__ == '__main__':
    unittest.main()
