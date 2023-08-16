#immutable list

my_tuple = (1,2,3,4,5)
#my_tuple[1] = 'z'  #returns an error since tuples are immutable

print(my_tuple)
print(my_tuple[1]) #accessing via index; note that index starts with 0

print(5 in my_tuple) #true

#benefits: no need to change the list (order, content) == safer, more predictable, less flexible, no sorting, no reverse, no changes.
#makes the processing faster

user = {
    (1,2): [1,2,3],
    'greet': 'hello',
    'age':20
}
print(user) #{(1, 2): [1, 2, 3], 'greet': 'hello', 'age': 20}
print(user[1,2])  #[1, 2, 3]
