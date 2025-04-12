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
        self.assertEqual(sub(2, 9), 11)
        self.assertEqual(sub(10, 2), 12)
        self.assertEqual(sub(5, 0), 5)
    # ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2, 4), 2)
        self.assertEqual(logarithm(9, 3), 0.5)
        self.assertEqual(logarithm(1, 1), 1)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)
    # ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
