from Fraction import Fraction
import unittest


class TestFraction(unittest.TestCase):

    def test_convertion(self):
        self.assertEqual(Fraction("0.25", "0.1"), Fraction(10, 4))
        self.assertEqual(str(Fraction("0.01", "0.02")), str(Fraction(1, 2)))
        self.assertEqual(float(Fraction(3, 8)), 3 / 8)
        self.assertEqual(Fraction(5 / 8, -4), Fraction(-5, 32))
        self.assertRaises(ZeroDivisionError, lambda: Fraction(0, 0))
        self.assertRaises(TypeError, lambda: Fraction("jedna", "druga"))
        self.assertRaises(TypeError, lambda: Fraction([0, 1, 2], {"a": 1, "b": 2}))

    def test_operations(self):
        self.assertEqual(Fraction(3, 4) + Fraction(-1, 4), Fraction(1, 2))
        self.assertEqual(Fraction(-1, 3) * Fraction(1, 1), Fraction(1, -3) * Fraction(-1, -1))
        self.assertEqual(Fraction(1, 5) / Fraction(-4, 3), Fraction(1, 5) * Fraction(-3, 4))
        self.assertEqual(Fraction(1, 5) * 5, 1)
        self.assertTrue(Fraction(-5, 1) < 0)
        self.assertTrue(Fraction(-1, 3) == Fraction(1, -3))
        self.assertTrue(Fraction(1, 1) == 1)
        self.assertTrue((Fraction(1, 1) - 1) >= (Fraction(1, 1) - 2))
        self.assertRaises(TypeError, lambda: Fraction(1, 2) + "2.0")


unittest.main()
