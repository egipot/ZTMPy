# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 19:28:00 2022

@author: GayCalaranan
"""

# args **kwargs

#def super_func(args):
#    return sum(args)
#super_func(1,2,3,4,5) #this will produce and error that states "TypeError: super_func() takes 1 positional argument but 5 were given

def super_func(*args, **kwargs):
    print(args) #(1,2,3,4,5)
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

#print(super_func(1,2,3,4,5)) #15

print(super_func(1,2,3,4,5, num1=5, num2=10)) #30

#Rule on the order: params, *args, default parameters, **kwargs

