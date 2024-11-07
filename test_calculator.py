import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def testadd(self):
        self.assertEqual(self.calc.add(3, 5), 8)
        self.assertEqual(self.calc.add(4, 9), 13)

    def testsubtract(self):
        self.assertEqual(self.calc.subtract(6, 8), -2)
        self.assertEqual(self.calc.subtract(16, 4), 12)

    def testmultipy(self):
        self.assertEqual(self.calc.multiply(6, 3), 18)
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def testdivide(self):
        self.assertEqual(self.calc.divide(30, 2), 15)
        self.assertEqual(self.calc.divide(16, 4), 4)

    def testmodulo(self):
        self.assertEqual(self.calc.modulo(6, 5), 1)
        self.assertEqual(self.calc.modulo(16, 4), 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)