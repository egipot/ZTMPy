#set = unordered collection of unique objects/values
#set uses {}
#no key:value pair. just values
#does not support indexing so checking only the exact value(not the index)


my_set = {1,2,3,4,5,5}
print(my_set) #returns only the unique values = {1, 2, 3, 4, 5}



my_set.add(100)
my_set.add(2)
print(my_set) #returns {1, 2, 3, 4, 5, 100} ; 2 does not need to be added since this value already exists in the set

my_list = [1,2,3,4,5,5]
print((set(my_list))) # returns the unique elements in the list by converting that list into a set == {1, 2, 3, 4, 5} 

print(1 in my_set) #true
print(7 in my_set) #false
print(len(my_set)) #6

#converting to list
new_set = my_set.copy()
print(new_set)
print(list(new_set))