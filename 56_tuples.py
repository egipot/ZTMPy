my_tuple = (1,2,3,4,5,5)
new_tuple = my_tuple[1:2]

print(new_tuple)

x = my_tuple[0]
y = my_tuple[1]
print(x)
print(y)

#another method (quicker than above)
a, b, c, *other =  (1,2,3,4,5)
print(a)
print(b)
print(other)

#count
#index

print(my_tuple.count)
print(my_tuple.count(5)) #2
print(my_tuple.index(5)) #4 - returns index of the first instance of that value
print(len(my_tuple)) #6

#TUPLES ARE LISTS THAT ARE IMMUTABLE