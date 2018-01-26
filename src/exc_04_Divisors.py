'''
Created on Dec 10, 2017

@author: antonina

Description:

Create a program that asks the user for a number and then 
prints out a list of all the divisors of that number. 

(If you don’t know what a divisor is, it is a number that divides evenly into another number. 
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''

from src.exc_02_OddOrEven import getInteger

def getAllDivisors(n):
    'Returns a list of all the divisors of number n'
    try:
        if int(n) >= 0:
            return [i for i in range(1, n) if n % i == 0]
        else:
            return [i for i in range(-1, n, -1) if n % i == 0]
    except TypeError:
        return None
        

def main():
    
    print("Printing out all divisors of a number provided below:")
    print(getAllDivisors(getInteger('Input any integer number: ')))
    
    
if __name__ == "__main__":
    main()
    
    
    