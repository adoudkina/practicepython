'''
Created on Dec 11, 2017

@author: antonina
'''
from src.exc_02_OddOrEven import *

import unittest
from unittest.mock import patch


class GetIntegerTest(unittest.TestCase):
    
    @patch('builtins.input')
    def test_inputOne(self, mock_input):
        '''If user inputs 1 - number 1 is returned'''
        mock_input.return_value = '1'
        self.assertEqual(getInteger('Custom User Input message'), 1)
    
        
    @patch('builtins.input')
    def test_inputMinusOne(self, mock_input):
        '''If user inputs -1 - number -1 is returned'''
        mock_input.return_value = '-1'
        self.assertEqual(getInteger('Custom User Input message'), -1)
     
        
    @patch('builtins.print')
    @patch('builtins.input')    
    def test_inputFloat(self, mock_input, mock_print):
        '''If user inputs float 1.1 - None is returned and appropriate message is printed'''
        mock_input.return_value = '1.1'
        self.assertIsNone(getInteger('Custom User Input message'))   
        mock_print.assert_called_with('Your input is invalid. Only integer numbers are expected.')
    
    
    @patch('builtins.print')    
    @patch('builtins.input')
    def test_inputText(self, mock_input, mock_print):
        '''If user inputs text - None is returned and appropriate message is printed'''
        mock_input.return_value = 'one'
        self.assertIsNone(getInteger('Custom User Input message'))
        mock_print.assert_called_with('Your input is invalid. Only integer numbers are expected.')


class IsEvenTests(unittest.TestCase):
    ''' Unit test for function 'isEven(number)'
    Returns True if number is even, otherwise False
    ''' 
    def test_MinusHundredIsEven(self):
        self.assertTrue(isEven(-100), "-100 is even")
        
    def test_MinusOneIsNotEven(self):
        self.assertFalse(isEven(-1), "-1 is not even")
     
    def test_ZeroIsEven(self):
        self.assertTrue(isEven(0))
        
    def test_OneIsNotEven(self):
        self.assertFalse(isEven(1)) 
          
    def test_SixIsEven(self):
        self.assertTrue(isEven(6))

    def test_FloatIsNotEven(self):
        self.assertFalse(isEven(6.6))


class IsDividedEvenlyTests(unittest.TestCase):
    
    
    def test_SixDividesThree(self):
        self.assertTrue(isDividedEvenly(6, 3))
    
    def test_FourDoesnotDivideThree(self):
        self.assertFalse(isDividedEvenly(4, 3))


if __name__ == '__main__':
    unittest.main()

