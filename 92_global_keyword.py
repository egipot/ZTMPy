# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 10:19:15 2022

@author: GayCalaranan
"""

a = 10

def parent(b):
    print(b) #300
    a = 90


print(parent(300)) #None
print(a) #10
#print(b) #not defined globally


# 1 start with local
# 2 parent or local?
# 3 Global
#4 built in python functions e.g sum --> prints "built-in function sum"

#=================

total = 0

def count():
    global total
    total += 1
    return total

count()
count()
print(count())