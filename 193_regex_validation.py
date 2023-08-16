# https://emailregex.com/
# r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"


#r" " = ensures that Python considers the while string as simple string (no special function/meaning such as new line for \n)
# r"(^[a-zA-Z0-9_.+-]+@[organization]+\.[a-zA-Z0-9-.]+$)"
# sdfadsfa@organization.com

import re

first = input("Enter the first name: ")
last = input("Enter the last name: ")

pattern = re.compile(r'(^[a-zA-Z0-9_.+-]+@[organization]+\.[a-zA-Z0-9-.]+$)')
fullname = first + "." + last
string = 'abc.def@organization.com'

a = pattern.search(string)
print(a)
print(a.group())
