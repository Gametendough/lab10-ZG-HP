#https://github.com/Gametendough/lab10-ZG-HP/tree/main
#Partner 1: Zachary Gonzalez
#Partner 2: Hansita Penikalapati

import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(3,5), 8)
        self.assertEqual(add(-2, 4), 2)
        self.assertEqual(add(6, 0), 6)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(2, 9), -7)
        self.assertEqual(subtract(10, 2), 8)
        self.assertEqual(subtract(5, 0), 5)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(5, 3), 15)
        self.assertEqual(mul(8, 3), 24)
        self.assertEqual(mul(-4, 7), -28)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(24, 4), 6)
        self.assertEqual(div(-12, -4), 3)
        self.assertEqual(div(2, 2), 1)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2, 4), 2)
        self.assertEqual(logarithm(9, 3), 0.5)
        self.assertEqual(logarithm(2, 1), 0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(10, 1)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(4, 12.37), 13)
        self.assertAlmostEqual(hypotenuse(8.66, 5), 10)
        self.assertAlmostEqual(hypotenuse(.001, 18), 18)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(81), 9)
        self.assertEqual(square_root(36), 6)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
