from simple_calculator import SimpleCalculator
import unittest


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 3), 13)
        self.assertEqual(self.calc.add(20, 45), 65)
        self.assertEqual(self.calc.add(30, 3), 33)
        self.assertEqual(self.calc.add(16, -1), 15)
        self.assertEqual(self.calc.add(18, -20), -2)
    
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(2, 3), -1)
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(20, 45), -25)
        self.assertEqual(self.calc.subtract(30, 3), 27)
        self.assertEqual(self.calc.subtract(16, -1), 17)
        self.assertEqual(self.calc.subtract(18, -20), 38)
    
    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(10, 3), 30)
        self.assertEqual(self.calc.multiply(20, 45), 900)
        self.assertEqual(self.calc.multiply(30, 3), 90)
        self.assertEqual(self.calc.multiply(16, -1), -16)
        self.assertEqual(self.calc.multiply(18, -20), -360)
    
    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(3, 3), 1)
        self.assertEqual(self.calc.divide(9, 3), 3)
        self.assertEqual(self.calc.divide(18, 3), 6)
        self.assertEqual(self.calc.divide(30, 3), 10)
        self.assertEqual(self.calc.divide(42, 6), 7)
        self.assertEqual(self.calc.divide(49, 7), 7)


if __name__ == '__main__':
    unittest.main()
        