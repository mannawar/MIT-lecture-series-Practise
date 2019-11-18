# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 22:11:57 2019

@author: Mannawar Hussain
"""

def is_even_with_return(i):
    '''
    Input: i, a positive int
    Returns True if i is even, otherwise False
    '''
    print ('with_return')
    remainder = i % 2
    return remainder == 0
is_even_with_return(4) 
print(is_even_with_return(4))



def is_even_without_return(i):
    '''
    Input: i, a positive int
    Does not return anything
    '''
    print ('without_return')
    remainder = i % 2
    
is_even_without_return(4) 
print(is_even_without_return(4))






print ("All numbers between 0 and 20: even or not")
for i in range (20):
    if is_even(i):
        print (i, "even")
    else:
        print (i, "odd")
        
        
def func_a():
    print ('inside func_a') 

def func_b(y):
    print ('inside func_b')
    return y

def func_c(z):
    print('inside func_c')
    return z()

print(func_a())
print(5+func_b(2))
print(func_c(func_a))      
    

















