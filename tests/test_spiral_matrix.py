import unittest

from solutions.spiral_matrix import spiral_matrix


class TestSpiralMatrix(unittest.TestCase):
    def test_make_spiral_with_size_1(self):
        expected = [[1]]
        actual = spiral_matrix(1)
        self.assertEqual(expected, actual)

    def test_make_spiral_with_size_2(self):
        expected = [
            [1, 2],
            [4, 3],
        ]
        actual = spiral_matrix(2)
        self.assertEqual(expected, actual)

    def test_make_spiral_with_size_3(self):
        expected = [
            [1, 2, 3],
            [8, 9, 4],
            [7, 6, 5],
        ]
        actual = spiral_matrix(3)
        self.assertEqual(expected, actual)

    def test_make_spiral_with_size_4(self):
        expected = [
            [1, 2, 3, 4],
            [12, 13, 14, 5],
            [11, 16, 15, 6],
            [10, 9, 8, 7],
        ]
        actual = spiral_matrix(4)
        self.assertEqual(expected, actual)

    def test_make_spiral_with_size_5(self):
        expected = [
            [1, 2, 3, 4, 5],
            [16, 17, 18, 19, 6],
            [15, 24, 25, 20, 7],
            [14, 23, 22, 21, 8],
            [13, 12, 11, 10, 9],
        ]
        actual = spiral_matrix(5)
        self.assertEqual(expected, actual)

    def test_make_spiral_with_size_6(self):
        expected = [
            [1, 2, 3, 4, 5, 6],
            [20, 21, 22, 23, 24, 7],
            [19, 32, 33, 34, 25, 8],
            [18, 31, 36, 35, 26, 9],
            [17, 30, 29, 28, 27, 10],
            [16, 15, 14, 13, 12, 11],
        ]
        actual = spiral_matrix(6)
        self.assertEqual(expected, actual)

    def test_make_spiral_with_size_7(self):
        expected = [
            [1, 2, 3, 4, 5, 6, 7],
            [24, 25, 26, 27, 28, 29, 8],
            [23, 40, 41, 42, 43, 30, 9],
            [22, 39, 48, 49, 44, 31, 10],
            [21, 38, 47, 46, 45, 32, 11],
            [20, 37, 36, 35, 34, 33, 12],
            [19, 18, 17, 16, 15, 14, 13],
        ]
        actual = spiral_matrix(7)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
