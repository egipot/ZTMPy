my_set = {1,2,3,4,5,5}
your_set = {4,5,6,7,8,9,10}

#print(my_set.difference(your_set)) #ignores the duplicates, returns the different elements  --> returns {1, 2, 3}
#print(my_set) #returns the unique elements {1, 2, 3, 4, 5}
#print(your_set)

#print(my_set.discard(5)) #prints None
#print(my_set) #returns {1, 2, 3, 4} due to discarded elements with value == 5

#print(my_set.difference_update(your_set)) #None
#print(my_set) #updated so that the differences are removed {1, 2, 3} .e.g changed set

#all prints above are commented out
#print(my_set.intersection(your_set)) #returns {4,5}. Same as print(my_set & your_set)

#all prints above are commented out
#print(my_set.isdisjoint(your_set)) #false because there are common elements; This will return TRUE if there are no common elements

#all prints above are commented out
#print(my_set.intersection_update(your_set))


#print(my_set.union(your_set)) #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10} == combined the elements of the two sets and removed all duplicates, returning a new set; can also be done via |. Try by commenting this line
#print(my_set | your_set) #returns {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


#print(my_set.issubset(your_set))  #returns False
#my_set2 = {4,5}
#print(my_set2.issubset(your_set)) #returns True


#print(your_set.issuperset(my_set2)) #returns True


#all prints above are commented out
print(my_set.update(your_set)) #returns None
new_set3 = {101, 102}
print(new_set3)
new_set3.update(your_set) #update is done in the 1st set in the syntax i.e. no need to assign to a new set
print(new_set3)
