import unittest
from ruler import Ruler

class TestRuler(unittest.TestCase):
  
  _ruler = Ruler()
  def test_ruler(self):
    self.assertEqual("1", self._ruler.print_num(1))

  def test_ruler2(self):
    self.assertEqual("121", self._ruler.print_num(2))

  def test_ruler4(self):
    self.assertEqual("121312141213121", self._ruler.print_num(4))

if __name__ == '__main__':
  unittest.main()
