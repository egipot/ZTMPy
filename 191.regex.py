#https://www.w3schools.com/python/python_regex.asp
#https://regex101.com/ 
#https://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters 



import re

pattern = re.compile (r'([a-zA-Z]).([a])')
string = 'search this inside of this text please'

a = pattern.search(string)
print(a.group())  #sea
print(a.group(1)) #s
print(a.group(2)) #a

# ^ = start of the string
# $ = end of the string
# \d = any digit from 0 to 9
# . = wildcard = can match any single character
# \.
#  