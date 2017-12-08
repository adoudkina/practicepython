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

name = input("Input your name: ")

try:
    age = input("Input your age: ")
    repeat = input("How many times to repeat an answer: ")
    
    if int(age) and int(repeat):
        current_year = datetime.date.today().year
        years_till_100 = 100 - int(age)
        reply = name + ', you will turn 100 years old in ' + str(current_year+years_till_100) + ' year\n'
        print(reply*int(repeat))

except ValueError as e:
    print(e)
    
