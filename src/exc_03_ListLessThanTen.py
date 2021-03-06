'''
Created on Dec 10, 2017

@author: antonina

Description:

Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

and write a program that prints out all the elements of the list that are less than 5.

Extras:

    Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
    Write this in one line of Python.
    Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

'''

from src.exc_02_OddOrEven import getInteger

def listLessThanN(t_list, n):
    'Returns a new list which comprises of all elements of t_list that are smaller than n'
    try:
        return [i for i in t_list if i < n]
    except TypeError as e:
        print(e)
        return None


def main():
    
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print('Initial list:', a)
    print('Printing only elements less than 5:', end = ' ')  
    [print(e, end=' ') for e in a if e < 5]
   
    'Extras'
    number = getInteger('\nInput integer number:') 
    print("Printing all elements less than {}:".format(number), listLessThanN(a, number))
    
    
if __name__ == "__main__":
    main()
    