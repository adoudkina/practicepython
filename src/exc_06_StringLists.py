'''
Created on Dec 10, 2017

@author: antonina

Description:

Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)
'''

def isPalindrome(str):
    'Returns True if string in argument is palindrome, otherwise returns False'
    '''
    for i in range(len(str) // 2):
        if not str[i] == str[-1-i]:
            return False
    return True  '''
    
    '''Improved solution:'''
    if str == str[::-1]:
        return True
    else:
        return False
      

def main():
    
    for i in range(5):
        test_str = input("Input string to test if it is palindrome: ").strip()
        print(isPalindrome(test_str))
        

if __name__ == "__main__":
    main() 
