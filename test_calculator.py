import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:

    #Add_Testing
    def test_add_Negative(self):
        self.assertEqual(self.calc.add(-1,-2),-3)
    def test_add_Zero(self):
        self.assertEqual(self.calc.add(1, 0), 1)

    #Subtrack_Testing
    def test_subtrack(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
    def test_subtack_Negativ(self):
        self.assertEqual(self.calc.subtract(-2, -1), -1)

    #Multiply_Testing
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5, 2), 10)
    def test_multiply_zero(self):
        self.assertEqual(self.calc.multiply(100, 0), 0)

    #Divide_Testing
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
    def test_divide_decimal(self):
        self.assertEqual(self.calc.divide(9, 8), 1)
        
    #Modulo_Testing
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 2), 0)
    def test_modulo_odd(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

if __name__ == '__main__':
    unittest.main()