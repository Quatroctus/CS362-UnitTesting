import unittest
from full_name import *

class TestFullName(unittest.TestCase):

    def test_normal(self):
        self.assertAlmostEqual(full_name("James", "Taylor"), "James Taylor")

    def test_integers(self):
        self.assertIsNone(full_name(346, 347))

    def test_bytes(self):
        self.assertIsNone(full_name(b'Hello', b'World'))

    def test_fail(self):
        """I'm not sure if this is what you want when you say 'Demonstrate pass and fail conditions'"""
        self.assertIsNone("Pepperoni", "Pizza")


if __name__ == "__main__":
    unittest.main()
