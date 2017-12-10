'''
Created on Dec 10, 2017

@author: antonina

Description:

Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 

Write one line of Python that takes this list a and makes a new list 
that has only the even elements of this list in it.
'''

def evenList(list1):
    'Accepts a list and returns a new list with only even elements in it'
    
    return [item for item in list1 if item % 2 == 0]

def main():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    print(evenList(a))
    

if __name__ == "__main__":
    main() 