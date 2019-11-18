# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 17:25:17 2019

@author: Mannawar Hussain
"""

a = int(input("Tell me one number: "))
b = int(input("Tell me another number: "))
print("a/b = ", a/b)
print("a+b = ", a+b)


# with try

try:
    a = int(input("Tell me one number: "))
    b = int(input("Tell me another number: "))
    print("a/b = ", a/b)
except:
    print("Bug in user input.")
    
    
    















def is_even(n):
    """ 
    Returns True if a number is even
    and False if not 
    """
    if n > 0 and n % 2 == 0:
        return True
    elif n < 0 and n % 2 == 0:
        return True
    else: 
        return False
    
print("is_even(n):", 4)



c = coordinate(3,4)   
print (c)














