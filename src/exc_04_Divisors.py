'''
Created on Dec 10, 2017

@author: antonina

Description:

Create a program that asks the user for a number and then 
prints out a list of all the divisors of that number. 

(If you don’t know what a divisor is, it is a number that divides evenly into another number. 
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''

from exc_02_OddOrEven import getOneNumber

def getAllDivisors(n):
    'Returns a list of all the divisors of number n'
    
    return [i for i in range(1, n) if n % i == 0]


def main():
    
    print("Printing out all divisors of a number provided below:")
    print(getAllDivisors(getOneNumber()))
    
    
if __name__ == "__main__":
    main()
    
    
    