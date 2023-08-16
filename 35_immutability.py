#Strings are immutable

store_string = '01234567'
store_string[0] = '8'
print(store_string) 
#^ This returns a TypeError: 'str' object does not support item assignment == because strings are immutable. 
#The only way to change is to create something new