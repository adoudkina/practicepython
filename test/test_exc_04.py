'''
Created on Jan 26, 2018

@author: antonina
'''
import unittest
from src.exc_04_Divisors import getAllDivisors


class DivisorListTest(unittest.TestCase):

    def test_successfully_return_all_divisors_for78(self):
        expected_list = [1, 2, 3, 6, 13, 26, 39]
        self.assertListEqual(getAllDivisors(78), expected_list)
        
    def test_successfully_return_all_divisors_for_minus78(self):
        expected_list = [-1, -2, -3, -6, -13, -26, -39]
        self.assertListEqual(getAllDivisors(-78), expected_list)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()