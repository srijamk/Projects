import unittest
from physics import Physics

class TestDisplacement(unittest.TestCase):
  def test_displacement(self):
    object = Physics()
    self.assertEqual(6.890165, object.displacement(1, 1, 1))

if __name__ == '__main__':
  unittest.main()
