import unittest

from solutions.expression_evaluator import calculate


class TestExpressionEvaluator(unittest.TestCase):
    def test_simple_addition(self):
        expected = 15
        actual = calculate("10+5")
        self.assertEqual(expected, actual)

    def test_positive_sign_addition(self):
        expected = 15
        actual = calculate("+10+5")
        self.assertEqual(expected, actual)

    def test_negative_sign_addition(self):
        expected = -5
        actual = calculate("-10+5")
        self.assertEqual(expected, actual)

    def test_simple_subtraction(self):
        expected = 5
        actual = calculate("15-10")
        self.assertEqual(expected, actual)

    def test_multiplication(self):
        expected = 50
        actual = calculate("10*5")
        self.assertEqual(expected, actual)

    def test_division(self):
        expected = 2
        actual = calculate("10/5")
        self.assertEqual(expected, actual)

    def test_double_division(self):
        expected = 1
        actual = calculate("8/4/2")
        self.assertEqual(expected, actual)

    def test_mixed_operations(self):
        expected = 17
        actual = calculate("10+5*2-3")
        self.assertEqual(expected, actual)

    def test_mixed_operations2(self):
        expected = 22
        actual = calculate("10+2*3+6")
        self.assertEqual(expected, actual)

    def test_decimal_numbers(self):
        expected = 4.5
        actual = calculate("9/2")
        self.assertEqual(expected, actual)

    def test_no_operation(self):
        expected = 6
        actual = calculate("6")
        self.assertEqual(expected, actual)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            calculate("6+1a")

    def test_parentheses_not_allowed(self):
        with self.assertRaises(ValueError):
            calculate("(3+4)*2")


if __name__ == "__main__":
    unittest.main()
