user = {
    'basket' : [1,2,3],
    'greet' : 'hello',
    'age' : 20
}
print('age' in user) #true
print('size' in user) #false

print('size' in user.keys()) #false
print(20 in user.values()) #true
print(user.items()) #returns a tuple

#print(user.clear()) #None
#print(user) # {}

user2 = print(user.copy())
print(user)
print(user2)

print(user.pop('age')) #20
print(user) #{'basket': [1, 2, 3], 'greet': 'hello'}

#print(user.popitem()) #removes the last item (e.g. last key:value pair that was inserted into the dictionary); so no longer random since Python 3.7
#print(user)

print(user.update({'basket':55}))
print(user.update({'ages':22}))
print(user)