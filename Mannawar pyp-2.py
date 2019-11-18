# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 10:57:33 2019

@author: Mannawar Hussain
"""
# More understanding of a string in python
types_of_people = 10
x = f"There are {types_of_people} types of people." # string1
binary = "binary" # assigning value to the variable in left
do_not = "don't" # assigning value to variable in left
y= f"Those who who know {binary} and those who {do_not}." #string2
print (x) # publish string x
print (y) # publish string y
print (f"If I said: {x}") # string 3
print (f"If i also said: {y}")# string 4
hilarious = True # Assign a value to the variable

joke_evaluation = "Isn't that joke so funny?! {}" # Assign a value to the variable


print (joke_evaluation.format(hilarious) )# .format assign a value to already created string

w = "This is left side of..." # Assign a value to the variable

e = "a string with right side." # Assign a value to the variable

print (w+e) # print the value of strings after concatenation/addition