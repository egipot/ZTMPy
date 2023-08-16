# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 20:24:42 2022

@author: https://replit.com/@aneagoie/walrus#main.py
"""

#walrus :=
# https://docs.python.org/3/whatsnew/3.8.html

#There is new syntax := that assigns values to variables as part of a larger expression. It is affectionately known as “the walrus operator” due to its resemblance to the eyes and tusks of a walrus.

#In this example, the assignment expression helps avoid calling len() twice:

#if (n := len(a)) > 10:
#    print(f"List is too long ({n} elements, expected <= 10)")
#######################################################

a = 'helloooooooooo'

if ((n := len(a)) > 10):
    print(f"too long {n} elements")

while ((n := len(a)) > 1):
    print(n)
    a = a[:-1]

print(a)