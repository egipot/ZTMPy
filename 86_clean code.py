# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 19:21:31 2022

@author: GayCalaranan
"""

#not clean code
def is_odd_or_even(num):
    if num % 2 == 0:
        return True
    elif num % 2 != 0:
        return False
    
print(is_odd_or_even(51))


#cleanER code
def is_odd_or_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
print(is_odd_or_even(51))


#cleanEST code
def is_odd_or_even(num):
    if num % 2 == 0:
        return True
    return False
    
print(is_odd_or_even(51))


#cleanEST cleanest code
def is_odd_or_even(num):
    return num % 2 == 0
      
    
print(is_odd_or_even(51))