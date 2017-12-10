'''
Created on Dec 10, 2017

@author: antonina

Description:

Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.

Extras:

    Randomly generate two lists to test this
    Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

'''

import random

def getOverlappingList(list1, list2):
    'Returns a new list that contains only common elements between list1 and list2'
    
    overlap_list = list()
    
    for i in range(len(list1)):
            if (list1[i] in list2) and (list1[i] not in overlap_list):
                    overlap_list.append(list1[i])
                
    return overlap_list
 
    #return [list1[i] for i in range(len(list1)) if list1[i] in list2]

def generateList(size):
    'Returns a new list with randomly generated elements of size passed as an argument'
    
    return [random.randint(-20,20) for i in range(size)]
    

def main():
    
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    
    print("List 1:", a, "\nList2:", b) 
    print("Common elements between two lists:", getOverlappingList(a, b))
    
#---------------------------------------------------------------------------   
    print("-" * 50)
    c = generateList(18)
    d = generateList(25)
    print("Generated 1st list:", c, "\nGenerated 2nd list:", d)
    print("Common elements between two lists:", getOverlappingList(c, d))

if __name__ == "__main__":
    main()    