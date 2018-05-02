#!/usr/bin/python3.4
import unittest
from Experiment3 import Greeter

class MyTestCase(unittest.TestCase):
    def test_default_greeting_set(self):
        greeter = Greeter()
        self.assertEqual(greeter.message, "This is a message")

if __name__ == '__main__':
    unittest.main()
