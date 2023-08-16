# https://www.w3schools.com/python/python_regex.asp

import re

pattern = re.compile ('search this inside of this text please')
string = 'search this inside of this text please Andrei'
print('search' in string) #True

#re.search (pattern, string, flags)
a = re.search('this', string)
print(a.span())     #(7, 11)
print(a.start())    #7
print(a.end())      #11
print(a.group())    #this

b = re.findall('this', string)
print(b)            #['this', 'this']

c = pattern.search (string)
print(c.group())    #<built-in method group of re.Match object at 0x0000012CCFB73B90>

d = pattern.fullmatch(string)
print(d)            #None
e = pattern.match(string)
print(e.group())    #search this inside of this text please


