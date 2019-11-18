# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 10:11:31 2019

@author: Mannawar Hussain
"""

def add (x, y):
    return (x+y)

def mult (x,y):
    print (x*y)
    
add(1, 2)
print (add(2,3))
mult(3,4)
print (mult(4,5))




print(type(5))
print(3.0-1)


x + y = 2

x*x = 2

2 = x

xy =2



#exercise 3-lecture 1

    usa_gold = 46
    uk_gold = 27
    romania_gold = 1
    
    total_gold = usa_gold + uk_gold + romania_gold
    print(total_gold)
    
    romania_gold += 1
    total_gold = usa_gold + uk_gold + romania_gold
    print(total_gold)
    

#Lecture 2 Q-2 comparison
pset_time = 15
sleep_time = 8
print (sleep_time > pset_time)  
derive = True
drink = False
both = drink and derive
print(both)
    




s1= (1,2,3)
s2= (2)
s1 and s2
s1 or s2    
s1 != s2   
    









# Branching

x = float(input("Enter a number for x: "))
y = float(input("Enter a number for y: "))
if x == y:
    if y != 0:
        print("x / y is", x/y)
elif x < y:
    print("x is smaller")
else:
    print("y is smaller")
    
    
    








#while loops
n = input("You're in the Lost Forest. Go left or right? ")
while n == "right" or n == "right":
    n = input("You're in the Lost Forest. Go left or right? ")
print("You got out of the Lost Forest!")




#for loops

mysum = 0
for i in range(5, 11, 2):
    mysum += i
    if mysum == 5:
        break
        mysum += 1
print(mysum)









# Lecture 3 q-1

s = "6.00 is 6.001 and 6.002"
new_str = ""
new_str += s[-1]
new_str += s[0]
new_str += s[4::30]    
new_str += s[13:10:-1]
print(new_str)





q-2

s1 = "mit u rock"
s2 = "i rule mit"
if len(s1) == len(s2):
    for char1 in s1:
        for char2 in s2:
            if char1 == char2:
                print("common letter")
                break# this break will not allow to check other characters in program once mapped in both s1 and s2
















    