#zip = useful in combining similarly arranged AND Equal amount of data in one tuple (data structure)
#zip iterates in all lists to be iterated.
#zip does not modify the existing list, but it creates a new one
#if there size of list/tuple is not the same, resulting zip list is cut

my_list = [1,2,3,4]
your_list = [10, 20, 30]
their_tuple = (100, 200, 300, 400) #tuples can be zipped with lists too (same handling)
def multiply_by2(item):
    return item*2 

def odd(item):
    return item % 2 !=0

print(list(zip(my_list, your_list, their_tuple)))  # [(1, 10, 100), (2, 20, 200), (3, 30, 300)]  
print(my_list)   # [1, 2, 3, 4]