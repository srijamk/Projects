import unittest
from stars_and_numbers_two import StarsAndNumbers

class TestStarsandNumbers(unittest.TestCase):
  def test_stars_and_numbers(self):
    number = StarsAndNumbers()

    self.assertEqual("***\n** \n* *\n", number.stars_and_numbers(3))

if __name__ == '__main__':
  unittest.main()
