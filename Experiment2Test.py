#!/usr/bin/python2.7
import unittest
from Experiment2 import Greeter

class MyTestCase(unittest.TestCase):
    def test_default_greeting_set(self):
        greeter = Greeter()
        self.assertEqual(greeter.message, "Python 2.7.6")

if __name__ == '__main__':
    unittest.main()
