import unittest
from dragon_curves import DragonCurves

class TestDragonCurves(unittest.TestCase):
  def test_dragon_curves(self):
    paper = DragonCurves()
    self.assertEqual("F", paper.dragon_curves(0))
    self.assertEqual("FLF", paper.dragon_curves(1))
    self.assertEqual("FLFLFRF", paper.dragon_curves(2))
    self.assertEqual("FLFLFRFLFLFRFRF", paper.dragon_curves(3))

if __name__ == '__main__':
  unittest.main()
