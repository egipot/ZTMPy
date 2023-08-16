# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 20:11:56 2022

@author: GayCalaranan
"""

def highest_even(li):
    highnum = []
    for value in li:
        if value % 2 == 0:
            highnum.append(value)
    return max(highnum)  
    

print(highest_even([10,2,3,4,8,11]))

#same answer with andrei, I just initialy forgot the return.
#be careful of the indention when to retun