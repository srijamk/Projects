import unittest
from binary_conversion import Binary

class TestBinary(unittest.TestCase):
  def test_binary(self):
    num = Binary()
    self.assertEqual("0", num.binary(0))
    self.assertEqual("1", num.binary(1))
    self.assertEqual("1010", num.binary(10))
if __name__ == '__main__':
  unittest.main()
