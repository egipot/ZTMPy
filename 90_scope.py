# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 20:34:13 2022

@author: GayCalaranan
"""

# scope = what variables do I have access to within a function?

#global scope:
#total = 100    


#if True:
x = 10

def some_func():
    total = 100    
    print (total)       #100
    print(x)            #10
    return total + x    #110

#print(x) #10
print(some_func())

