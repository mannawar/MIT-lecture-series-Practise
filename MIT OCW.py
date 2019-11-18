# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 21:58:07 2019

@author: Mannawar Hussain
"""

an_letters= "aefhilmnorsxAEFHILMNORSX"
word = input("I will cheer for you! Enter a word:")
times = int(input("Enthusiasm Level(1-10):"))

i=0
while i < len(word):
    char = word[i]
    if char is an_letters:
        print ("Give me an " + char + "!" +char)
    else:
        print ("Give me an " + char + "!" +char)
        
    i += 1
print("what does that spell?")
for i in range (times):
    print (word, "!!!")
    
    
 # another way to write the same thing   
    
an_letters= "aefhilmnorsxAEFHILMNORSX"
word = input("I will cheer for you! Enter a word:")
times = int(input("Enthusiasm Level(1-10):"))

for char in word:
    if char is an_letters:
        print ("Give me an " + char + "!" +char)
    else:
        print ("Give me an " + char + "!" +char)
        
print("what does that spell?")
for i in range (times):
    print (word, "!!!")
    
    
    
    
    
    
    
    
    
    
    
    
#perfect cube
cube = 27
cube = 8120601
for guess in range(cube+1):
    if guess**3 ==cube:
        print ("cube root of", cube, "is", guess)
        
        




# guess and check cube root
cube = 27
cube = 8120601
for guess in range(abs(cube)+1):
    if guess**3 >= abs(cube):
        break
if guess**3 != abs(cube):
    print (cube, 'is not a perfect cube')
else:
    if cube < 0:
        guess = -guess
        print ('cube root of'+str(cube)+ 'is'+str(guess))
        
        
    

















