import unittest
from calculator import addition, subtraction, multiplication, division


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addition(10,2),12)


    def test_subtraction(self):
        self.assertEqual(subtraction(10,2),8)


    def test_multiplication(self):
        self.assertEqual(multiplication(10,2),20)


    def test_division(self):
        self.assertEqual(division(10,2),5.0)


if __name__ == "__main__":
    unittest.main()
