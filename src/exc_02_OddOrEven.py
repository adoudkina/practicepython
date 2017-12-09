'''
Created on Dec 8, 2017

@author: antonina

Description:

Ask the user for a number. 
Depending on whether the number is even or odd, print out an appropriate message to the user. 
Hint: how does an even / odd number react differently when divided by 2?

Extras:

    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

'''

def getOneNumber():
    'Asks a user to input one integer number and \
    returns it if input was valid, otherwise returns None.'
    
    try:
        number = input("Input any integer number:")
        if int(number):
            return int(number)
        
    except (ValueError) as e:
        print("Your input is invalid:", e) 
         
    

def isEven(number):
    'Returns True if number is even, otherwise False'
    
    if number % 2 == 0:
        return True
    else:
        return False


def isMultipleOfFour(number):
    'Returns True if number is multiple of 4, otherwise False'
     
    if number % 4 == 0:
        return True
    else:
        return False  

def isDividedEvenly(n1, n2):
    'Returns True if 1st argument divides evenly by 2nd argument\
    otherwise returns None'  
    
    if n1 % n2 == 0:
        return True   
    
def main():

    for i in range(4):
        
        number1 = getOneNumber()
        
        if (number1):
            if isMultipleOfFour(number1):
                print("Number", number1, "is even and can be divided by 4")
            elif isEven(number1):
                print("Number", number1, "is even")
            else:
                print("Number", number1, "is odd")       
 
 
#--Extra task---

    print("Now you can check if one number (1st) can be evenly divided by another number (2nd):")
    number2 = getOneNumber()
    number3 = getOneNumber()
    
    if number2 and number3:
        if isDividedEvenly(number2, number3):
            print(number2, "is divided evenly by", number3)
        else:
            print(number2, "is NOT divided evenly by", number3)
            
       
if __name__ == "__main__":
    main()
