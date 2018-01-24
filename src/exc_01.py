'''
Created on Dec 6, 2017

@author: antonina

Description:
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:
    Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
    Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
'''

import datetime 

while True:
    name = input("Input your name: ")
    if name.isalpha():
        break

while True:
    try:
        age = int(input("Input your age: "))
        repeat = int(input("How many times to repeat an answer: "))
        current_year = datetime.date.today().year
        years_till_100 = 100 - age
        reply = '{}, you will turn 100 years old in {} year\n'.format(name, str(current_year+years_till_100))
        print(reply*repeat)
        break
    
    except ValueError as e:
        print(e)
        continue
    
