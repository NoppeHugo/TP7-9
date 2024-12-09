import unittest
from fractions import Fraction

class TestFraction(unittest.TestCase):
    def test_initialization(self):
        self.assertEqual(str(Fraction(3, 4)), "3/4")
        self.assertEqual(str(Fraction(6, 8)), "3/4")  # Simplified
        self.assertEqual(str(Fraction(-2, 4)), "-1/2")
        self.assertEqual(str(Fraction(4, -8)), "-1/2")
        self.assertEqual(str(Fraction(0, 1)), "0")
        
    def test_zero_denominator(self):
        with self.assertRaises(ValueError):
            Fraction(1, 0)

    def test_as_mixed_number(self):
        self.assertEqual(Fraction(7, 3).as_mixed_number(), "2 1/3")
        self.assertEqual(Fraction(-7, 3).as_mixed_number(), "-2 1/3")
        self.assertEqual(Fraction(6, 3).as_mixed_number(), "2")

    def test_addition(self):
        self.assertEqual(Fraction(1, 2) + Fraction(1, 3), Fraction(5, 6))
        self.assertEqual(Fraction(1, 4) + Fraction(-1, 4), Fraction(0, 1))

    def test_subtraction(self):
        self.assertEqual(Fraction(3, 4) - Fraction(1, 4), Fraction(1, 2))
        self.assertEqual(Fraction(1, 2) - Fraction(3, 4), Fraction(-1, 4))

    def test_multiplication(self):
        self.assertEqual(Fraction(2, 3) * Fraction(3, 4), Fraction(1, 2))
        self.assertEqual(Fraction(-1, 2) * Fraction(2, 3), Fraction(-1, 3))

    def test_division(self):
        self.assertEqual(Fraction(1, 2) / Fraction(2, 3), Fraction(3, 4))
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 2) / Fraction(0, 1)

    def test_equality(self):
        self.assertTrue(Fraction(2, 3) == Fraction(4, 6))
        self.assertFalse(Fraction(2, 3) == Fraction(3, 4))

    def test_float_conversion(self):
        self.assertAlmostEqual(float(Fraction(1, 2)), 0.5)
        self.assertAlmostEqual(float(Fraction(2, 3)), 0.6666666666666666)

    def test_is_zero(self):
        self.assertTrue(Fraction(0, 1).is_zero())
        self.assertFalse(Fraction(1, 2).is_zero())

    def test_is_integer(self):
        self.assertTrue(Fraction(4, 2).is_integer())
        self.assertFalse(Fraction(3, 2).is_integer())

    def test_is_proper(self):
        self.assertTrue(Fraction(1, 2).is_proper())
        self.assertFalse(Fraction(3, 2).is_proper())

    def test_is_unit(self):
        self.assertTrue(Fraction(1, 3).is_unit())
        self.assertFalse(Fraction(2, 3).is_unit())

    def test_is_adjacent_to(self):
        self.assertTrue(Fraction(1, 2).is_adjacent_to(Fraction(1, 3)))
        self.assertFalse(Fraction(1, 2).is_adjacent_to(Fraction(2, 3)))

if __name__ == "__main__":
    unittest.main()
