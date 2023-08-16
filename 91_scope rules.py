# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 10:09:17 2022

@author: GayCalaranan
"""

#Scope - what variables do I have access to?

a = 1

def confusion():
    a = 5
    return a

print(a)
print(confusion())

def parent():
    a = 10
    def child():
        return sum
    return child()

print(parent())
print(a)

# 1 start with local
# 2 parent or local?
# 3 Global
#4 built in python functions e.g sum --> prints "built-in function sum"

