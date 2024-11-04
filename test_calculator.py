import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -2), -3)
    def test_add_zero(self):
        self.assertEqual(self.calc.add(1, 0), 1)
    # Add the following test methods to the TestCalculator class:

    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(-1, -2), 1)
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
    def test_subtract_lessthanzero(self):
        self.assertEqual(self.calc.subtract(3, 5), -2)

    def test_multiply_negativeall(self):
        self.assertEqual(self.calc.multiply(-5, -2), 10)
    def test_multiply_negativehalf(self):
        self.assertEqual(self.calc.multiply(-5, 2), -10)
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5, 0), 0)

    def test_divide_negativeall(self):
        self.assertEqual(self.calc.divide(-10, -2), 5)
    def test_divide_negativehalf(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
    def test_divide_notall(self):
        self.assertEqual(self.calc.divide(13, 3), 4)
    def test_divide_zero(self):
        self.assertEqual(self.calc.divide(13, 0), "Cannot divide by zero")

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)
    def test_modulo_negativehalf(self):
        self.assertEqual(self.calc.modulo(-11, 2), 1)
    def test_modulo_negativehalf2(self):
        self.assertEqual(self.calc.modulo(11, -2), -1)
    def test_modulo_negative(self):
        self.assertEqual(self.calc.modulo(-11, -2), -1)
    def test_modulo_zero(self):
        self.assertEqual(self.calc.modulo(11, 0), "Cannot modulo by zero")
if __name__ == '__main__':
    unittest.main()