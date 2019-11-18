# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:34:30 2019

@author: Mannawar Hussain
"""

#linear search on unsorted list
def linear_search (L,e):
    found = False
    for i in range (len(L)):
        if e == L[i]:
            found = True
    return found



#linear search on sorted list
def search (L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False