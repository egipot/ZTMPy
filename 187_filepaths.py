# https://docs.python.org/3/library/pathlib.html

import pathlib
path_ = pathlib.Path(__file__).parent.resolve()
print(path_) #C:\Users\GayCalaranan.000\Documents\Programming\Udemy - Python - ZTM

#moving current sad.txt into a lower level folder
with open('app/sad.txt', mode = 'r') as my_file_read:
    print(my_file_read.read())

with open('/Users/GayCalaranan.000/Documents/Programming/Udemy - Python - ZTM/app/sad.txt', mode = 'r') as my_file_read:
    print(my_file_read.read())

with open('./app/sad.txt', mode = 'r') as my_file_read:
    print(my_file_read.read())

with open('../laugh.txt', mode = 'r') as my_file_read:
    print(my_file_read.read()) #laugh.txt is stored in the folder "/Users/GayCalaranan.000/Documents/Programming/ which is one level up 

# relative path     = app/sad.txt'
# full path         = /Users/GayCalaranan.000/Documents/Programming/Udemy - Python - ZTM/
# from the current  = ./ = go to 
# go back ..
