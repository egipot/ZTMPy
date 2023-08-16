import datetime
from array import array

print(datetime.date.today())  # 2023-08-12
print(datetime.time(5,34,2))  # 05:34:02

#list in python is sometimes referred to as array in other languages, but there is a difference
#list in python is dynamic, anytime a data is needed, list can be increased incrementally - resulting to slower performance
#arrays in python takes up less memory and processes faster - can optimize the code
#https://docs.python.org/3/library/array.html
arr = array('i',[1,2,3] )
print(arr)                      # array('i', [1, 2, 3])
print(arr[0])                   # 1
print(type(arr))                # <class 'array.array'>

