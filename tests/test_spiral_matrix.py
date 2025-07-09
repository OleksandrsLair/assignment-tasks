import unittest

from solutions.spiral_matrix import SpiralMatrix


class TestSpiralMatrix(unittest.TestCase):
    def test_make_spiral_with_size_1(self):
        expected = [[1]]
        matrix = SpiralMatrix(1)
        actual = matrix.make_spiral()
        self.assertEqual(expected, actual)

    def test_make_spiral_with_size_2(self):
        expected = [
            [1, 2],
            [4, 3],
        ]
        matrix = SpiralMatrix(2)
        actual = matrix.make_spiral()
        self.assertEqual(expected, actual)

    def test_make_spiral_with_size_3(self):
        expected = [
            [1, 2, 3],
            [8, 9, 4],
            [7, 6, 5],
        ]
        matrix = SpiralMatrix(3)
        actual = matrix.make_spiral()
        self.assertEqual(expected, actual)

    def test_make_spiral_with_size_4(self):
        expected = [
            [1, 2, 3, 4],
            [12, 13, 14, 5],
            [11, 16, 15, 6],
            [10, 9, 8, 7],
        ]
        matrix = SpiralMatrix(4)
        actual = matrix.make_spiral()
        self.assertEqual(expected, actual)

    def test_make_spiral_with_size_5(self):
        expected = [
            [1, 2, 3, 4, 5],
            [16, 17, 18, 19, 6],
            [15, 24, 25, 20, 7],
            [14, 23, 22, 21, 8],
            [13, 12, 11, 10, 9],
        ]
        matrix = SpiralMatrix(5)
        actual = matrix.make_spiral()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
