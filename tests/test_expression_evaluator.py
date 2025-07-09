import unittest

from solutions.expression_evaluator import calculate


class TestExpressionEvaluator(unittest.TestCase):
    def test_simple_addition(self):
        expected = "15"
        actual = calculate("10+5")
        self.assertEqual(expected, actual)

    def test_simple_subtraction(self):
        expected = "5"
        actual = calculate("15-10")
        self.assertEqual(expected, actual)

    def test_multiplication(self):
        expected = "50"
        actual = calculate("10*5")
        self.assertEqual(expected, actual)

    def test_division(self):
        expected = "2"
        actual = calculate("10/5")
        self.assertEqual(expected, actual)

    def test_mixed_operations(self):
        expected = "17"
        actual = calculate("10+5*2-3")
        self.assertEqual(expected, actual)

    def test_mixed_operations2(self):
        expected = "22"
        actual = calculate("10+2*3+6")
        self.assertEqual(expected, actual)

    def test_decimal_numbers(self):
        expected = "4.5"
        actual = calculate("9/2")
        self.assertEqual(expected, actual)

    def test_no_operation(self):
        expected = "6"
        actual = calculate("6")
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
