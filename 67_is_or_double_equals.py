# is or ==

# == double equals check for equality in value
print(True == 1)
print('' == 1) #empty string is falsey
print([] == 10.0) #empty array is falsey
print(10 == 10.0) #integer and float can be equal in numerical value
print([] == []) #sets can be compared and can be equal in elements
print('1' == 1) #string and integer/float are not equal even if seemingly similar in value


# "is" is a keyword, which checks if the value in memory is the same. 
#all are false!
print(True is 1)
print('' is 1) 
print([] is 10.0)  
print(10 is 10.0) 
print([] is []) #sets are stored in separate location/memory so these two empty lists are stored separately, even if they have similar elements
print('1' is 1) 

#True because all are equal
print(True is True)
print(1 is 1)
print('1' is '1')


