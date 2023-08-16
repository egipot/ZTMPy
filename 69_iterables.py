#iterable = an object or a collection of multiple elements/characters that can be iterated by going over one by one, e.g. one element/character at a time
#can be a list, set, dict, tuple, string
#int and float are not iterable

#example1:
#for item in (1,2,3,4,5):
#    for x in ['a', 'b', 'c']:
#        print(item, x)

user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

for item in user: #equivalent to referring to keys
    print(item)

for item in user.items():
    print(item)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)



#unpacking a tuple - long method
for item in user.items():
    keys, values = item
    print(keys, values)

#unpacking a tuple - short method
for keys, values in user.items():
    print(keys, values)
