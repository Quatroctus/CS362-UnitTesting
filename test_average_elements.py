import unittest
from average_elements import *

class TestAverageElements(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(average_elements([]), 0)
        raise

    def test_list(self):
        elems = [436, 267, 45.95, 456]
        self.assertAlmostEqual(average_elements(elems), 301.2375)

    def test_tuple(self):
        self.assertAlmostEqual(average_elements((345, 25)), 185)

    def test_fail(self):
        """I'm not sure if this is what you want when you say 'Demonstrate pass and fail conditions'"""
        self.assertIsNone(average_elements("Hello World"))


if __name__ == "__main__":
    unittest.main()
