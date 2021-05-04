import unittest
from cube_volume import *

class TestCubeVolume(unittest.TestCase):

    def test_normal(self):
        self.assertAlmostEqual(volume_cube(10), 1000)

    def test_negative(self):
        self.assertRaises(ValueError, volume_cube, -10)

    def test_complex(self):
        self.assertRaises(TypeError, volume_cube, 67 + 4j)

    def test_fail(self):
        """I'm not sure if this is what you want when you say 'Demonstrate pass and fail conditions'"""
        self.assertIsNone(volume_cube("75"))


if __name__ == "__main__":
    unittest.main()
