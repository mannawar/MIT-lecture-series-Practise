# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 05:20:51 2019

@author: Mannawar Hussain
"""

def bubble_sort(L):
    swap = False
    while not swap:  #outer while loop is for doing multiple passes untill no more swaps
        print('bubble_sort:' + str(L))
        swap = True
        for j in range (1, len(L)):   #inner for loop is doing for comparison
            if L[j-1]>L[j]:
                swap=False
                temp= L[j]
                L[j] = L[j-1]
                L[j-1] = temp

testlist =[5, 3, 1]
print('')
print(bubble_sort(testlist))
print(testlist)