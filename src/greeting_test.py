import unittest
from greeting import Greeting

class TestGreeting(unittest.TestCase):
    def test_hello(self):
      greet = Greeting()
      self.assertEqual("Hello Yoda", greet.hello("Yoda"))

if __name__ == '__main__':
    unittest.main()
