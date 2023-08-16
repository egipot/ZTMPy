# comprehensions
# usable in list, set, dictionary
# quick way to create loops, sets or dictionaries instaed of looping

#oldway ; without comprehension
my_list = []
for char in 'hello':
    my_list.append(char)
print(my_list)

#with comprehension
# param for param in iterable
my_list2 = [char2 for char2 in 'hello']
#print(my_list2)

my_list3 = [num for num in range(0,101)]
#print(my_list3)

my_list3 = [num*2 for num in range(0,101)]
#print(my_list3)

my_list4 = [num**2 for num in range(0,100) if num % 2 == 0]
print(my_list4)